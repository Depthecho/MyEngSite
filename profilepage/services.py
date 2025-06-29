from django.contrib.contenttypes.models import ContentType
from django.db.models import Q
from django.utils import timezone
from django.http import HttpRequest, HttpResponse
from django.contrib import messages
from django.shortcuts import redirect, HttpResponseRedirect
from django.contrib.auth import update_session_auth_hash, get_user_model
from django.contrib.auth.models import AbstractBaseUser
from django.forms import Form
from typing import Any, Dict, Optional, Type, Union, List
from django.db import models
from .models import Profile, Achievement, Friendship, Notification
from .forms import ProfileUpdateForm, CustomPasswordChangeForm, UserUpdateForm

User = get_user_model()


class ProfileUpdateHandler:
    def __init__(self, request: HttpRequest) -> None:
        self.request = request
        self.user = request.user
        self.profile = request.user.profile
        self.context = self.get_forms()

    def process_update(self) -> Optional[HttpResponse]:
        if 'update_profile_and_user' in self.request.POST:
            self.context['user_form'] = UserUpdateForm(self.request.POST, instance=self.user)
            self.context['profile_form'] = ProfileUpdateForm(self.request.POST, self.request.FILES,
                                                             instance=self.profile)

            if self.context['user_form'].is_valid() and self.context['profile_form'].is_valid():
                self.context['user_form'].save()
                self.context['profile_form'].save()
                messages.success(self.request, "Your profile has been updated!")
                return redirect('profile')
            else:
                messages.error(self.request, "Please correct the errors in the profile form.")
                return None

        elif 'change_password' in self.request.POST:
            self.context['password_form'] = CustomPasswordChangeForm(self.user, self.request.POST)

            if self.context['password_form'].is_valid():
                user = self.context['password_form'].save()
                update_session_auth_hash(self.request, user)
                messages.success(self.request, "Password updated successfully!")
                return redirect('profile')
            else:
                messages.error(self.request, "Please correct the errors in the password change form.")
                return None

        return None

    def get_forms(self) -> Dict[str, Form]:
        return {
            'user_form': UserUpdateForm(instance=self.user),
            'profile_form': ProfileUpdateForm(instance=self.profile),
            'password_form': CustomPasswordChangeForm(self.user)
        }

    def get_context(self) -> Dict[str, Any]:
        return self.context


class AchievementChecker:
    ACHIEVEMENT_THRESHOLDS: Dict[str, Dict[int, int]] = {
        'words': {1: 100, 2: 500, 3: 1500},
        'texts': {1: 50, 2: 150, 3: 500},
        'tests': {1: 50, 2: 150, 3: 500}
    }

    @classmethod
    def check_achievements(cls, user: AbstractBaseUser, profile: Profile) -> None:
        for badge_type in cls.ACHIEVEMENT_THRESHOLDS:
            cls._check_single_type(user, profile, badge_type)

    @classmethod
    def _check_single_type(
            cls,
            user: AbstractBaseUser,
            profile: Profile,
            badge_type: str
    ) -> None:
        attr_name: str = ""
        if badge_type == 'words':
            attr_name = "words_learned"
        elif badge_type == 'texts':
            attr_name = "texts_read"
        elif badge_type == 'tests':
            attr_name = "tests_completed"

        current_value: int = getattr(profile, attr_name, 0)

        for level, threshold in cls.ACHIEVEMENT_THRESHOLDS[badge_type].items():
            if current_value >= threshold:
                Achievement.objects.get_or_create(
                    user=user,
                    badge_type=badge_type,
                    level=level,
                    defaults={'achieved_at': timezone.now()}
                )


class ProfileService:
    def __init__(self, user: AbstractBaseUser) -> None:
        self.user: AbstractBaseUser = user

    def get_or_create_profile(self) -> Profile:
        profile, created = Profile.objects.get_or_create(
            user=self.user,
            defaults={
                'friends_count': 0,
                'followers_count': 0
            }
        )

        if created:
            FriendshipService.update_friends_count(self.user)
            FriendshipService.update_followers_count(self.user)

        return profile

    def check_achievements(self) -> bool:
        profile: Profile = self.get_or_create_profile()
        AchievementChecker.check_achievements(self.user, profile)
        return True


class FriendshipService:
    @staticmethod
    def get_friends(user: User) -> List[User]:
        friendships = Friendship.objects.filter(
            (Q(from_user=user) | Q(to_user=user)),
            status=Friendship.ACCEPTED
        ).select_related('from_user', 'to_user')

        return [f.from_user if f.from_user != user else f.to_user for f in friendships]

    @staticmethod
    def get_followers(user: User) -> models.QuerySet[User]:
        return User.objects.filter(
            friendship_requests_sent__to_user=user,
            friendship_requests_sent__status=Friendship.REQUESTED
        )

    @staticmethod
    def update_friends_count(user: User) -> None:
        count = Friendship.objects.filter(
            (Q(from_user=user) | Q(to_user=user)),
            status=Friendship.ACCEPTED
        ).count()
        Profile.objects.filter(user=user).update(friends_count=count)

    @staticmethod
    def update_followers_count(user: User) -> None:
        count = Friendship.objects.filter(
            to_user=user,
            status=Friendship.REQUESTED
        ).count()
        Profile.objects.filter(user=user).update(followers_count=count)

    @staticmethod
    def send_request(from_user: User, to_user: User) -> Friendship:
        if from_user == to_user:
            raise ValueError("You cannot send a request to yourself")

        existing = Friendship.objects.filter(
            Q(from_user=from_user, to_user=to_user) | Q(from_user=to_user, to_user=from_user)
        ).first()

        if existing:
            if existing.status == Friendship.REQUESTED:
                if existing.from_user == from_user:
                    raise ValueError("Request already sent")
                else:
                    raise ValueError("You have a pending request from this user. Accept it instead.")
            elif existing.status == Friendship.ACCEPTED:
                raise ValueError("Already friends")
            elif existing.status == Friendship.REJECTED:
                existing.status = Friendship.REQUESTED
                existing.save()
                friendship = existing
        else:
            friendship = Friendship.objects.create(
                from_user=from_user,
                to_user=to_user,
                status=Friendship.REQUESTED
            )

        FriendshipService.update_followers_count(to_user)

        NotificationService.create_notification(
            user=to_user,
            notification_type='FRIEND_REQUEST',
            title='New Friend Request',
            message=f'{from_user.username} wants to be your friend',
            related_object=friendship
        )

        return friendship

    @staticmethod
    def accept_request(friendship: Friendship) -> None:
        if friendship.status != Friendship.REQUESTED:
            raise ValueError("Only pending requests can be accepted")

        friendship.status = Friendship.ACCEPTED
        friendship.save()

        FriendshipService.update_friends_count(friendship.from_user)
        FriendshipService.update_friends_count(friendship.to_user)
        FriendshipService.update_followers_count(friendship.to_user)

    @staticmethod
    def reject_request(friendship: Friendship) -> None:
        if friendship.status != Friendship.REQUESTED:
            raise ValueError("Only pending requests can be rejected")

        friendship.status = Friendship.REJECTED
        friendship.save()
        FriendshipService.update_followers_count(friendship.to_user)

    @staticmethod
    def remove_friendship(user1: User, user2: User) -> None:
        Friendship.objects.filter(
            (Q(from_user=user1, to_user=user2) |
             Q(from_user=user2, to_user=user1)),
            status=Friendship.ACCEPTED
        ).delete()

        FriendshipService.update_friends_count(user1)
        FriendshipService.update_friends_count(user2)


class NotificationService:
    @staticmethod
    def create_notification(
            user: User,
            notification_type: str,
            title: str,
            message: str,
            related_object: Optional[models.Model] = None
    ) -> Notification:
        content_type = None
        object_id = None

        if related_object:
            content_type = ContentType.objects.get_for_model(related_object)
            object_id = related_object.id

        return Notification.objects.create(
            user=user,
            notification_type=notification_type,
            title=title,
            message=message,
            content_type=content_type,
            object_id=object_id
        )

    @staticmethod
    def get_unread_count(user: User) -> int:
        return Notification.objects.filter(user=user, is_read=False).count()

    @staticmethod
    def mark_as_read(notification_id: int, user: User) -> bool:
        print(f"DEBUG_SERVICE: mark_as_read called for notif ID {notification_id}")
        try:
            notification = Notification.objects.get(id=notification_id, user=user)
            print(f"DEBUG_SERVICE: Notification {notification.id} is_read BEFORE: {notification.is_read}")
            if not notification.is_read:
                notification.is_read = True
                notification.save()
                print(f"DEBUG_SERVICE: Notification {notification.id} marked as read and saved.")
                return True
            print(f"DEBUG_SERVICE: Notification {notification.id} already read.")
            return False
        except Notification.DoesNotExist:
            print(f"DEBUG_SERVICE: Notification {notification_id} DoesNotExist for user {user.username}")
            return False