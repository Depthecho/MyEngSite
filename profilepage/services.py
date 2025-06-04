from django.db.models import Q
from django.utils import timezone
from django.http import HttpRequest
from django.contrib import messages
from django.shortcuts import redirect, HttpResponseRedirect
from django.contrib.auth import update_session_auth_hash, get_user_model
from django.contrib.auth.models import AbstractBaseUser
from django.forms import Form
from typing import Any, Dict, Optional, Type, Union
from .models import Profile, Achievement, Friendship
from .forms import ProfileUpdateForm, CustomPasswordChangeForm

User = get_user_model()


class ProfileUpdateHandler:
    def __init__(self, request: HttpRequest) -> None:
        self.request: HttpRequest = request
        self.profile: Profile = request.user.profile

    def process_update(self) -> Union[Form, HttpResponseRedirect]:
        form: Optional[Form] = self._get_appropriate_form()

        if not form or not form.is_valid():
            return form

        self._save_form(form)
        self._add_success_message()
        return redirect('profile')

    def _get_appropriate_form(self) -> Optional[Union[ProfileUpdateForm, CustomPasswordChangeForm]]:
        """Determine which form was submitted based on request data."""
        if 'update_profile' in self.request.POST:
            return ProfileUpdateForm(
                self.request.POST,
                self.request.FILES,
                instance=self.profile
            )
        elif 'change_password' in self.request.POST:
            return CustomPasswordChangeForm(
                self.request.user,
                self.request.POST
            )
        return None

    def _save_form(self, form: Union[ProfileUpdateForm, CustomPasswordChangeForm]) -> None:
        """Save the appropriate form based on its type."""
        if isinstance(form, CustomPasswordChangeForm):
            user: AbstractBaseUser = form.save()
            update_session_auth_hash(self.request, user)
        else:
            form.save()

    def _add_success_message(self) -> None:
        """Add appropriate success message based on form type."""
        message: str = (
            "Password updated successfully!"
            if 'change_password' in self.request.POST
            else "Your profile has been updated!"
        )
        messages.success(self.request, message)

    def get_forms(self) -> Dict[str, Form]:
        """Get both profile and password forms."""
        return {
            'profile_form': ProfileUpdateForm(instance=self.profile),
            'password_form': CustomPasswordChangeForm(self.request.user)
        }


class AchievementChecker:
    ACHIEVEMENT_THRESHOLDS: Dict[str, Dict[int, int]] = {
        'words': {1: 100, 2: 500, 3: 1500},
        'texts': {1: 50, 2: 150, 3: 500},
        'tests': {1: 50, 2: 150, 3: 500}
    }

    @classmethod
    def check_achievements(cls, user: AbstractBaseUser, profile: Profile) -> None:
        """Check and create achievements for all badge types."""
        for badge_type in cls.ACHIEVEMENT_THRESHOLDS:
            cls._check_single_type(user, profile, badge_type)

    @classmethod
    def _check_single_type(
            cls,
            user: AbstractBaseUser,
            profile: Profile,
            badge_type: str
    ) -> None:
        """Check achievements for a single badge type."""
        attr_name: str = (
            f"{badge_type}_learned" if badge_type == 'words'
            else f"{badge_type}_read" if badge_type == 'texts'
            else f"{badge_type}_completed"
        )
        current_value: int = getattr(profile, attr_name)

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
        """Get or create user profile with defaults."""
        profile, created = Profile.objects.get_or_create(
            user=self.user,
            defaults={
                'username': self.user.username,
                'email': self.user.email,
                'first_name': '',
                'last_name': '',
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
    def get_friends(user):
        friendships = Friendship.objects.filter(
            (Q(from_user=user) | Q(to_user=user)),
            status=Friendship.ACCEPTED
        ).select_related('from_user', 'to_user')

        return [f.from_user if f.from_user != user else f.to_user for f in friendships]

    @staticmethod
    def get_followers(user):
        return User.objects.filter(
            friendship_requests_sent__to_user=user,
            friendship_requests_sent__status=Friendship.REQUESTED
        )

    @staticmethod
    def update_friends_count(user):
        """Обновить счетчик друзей"""
        count = Friendship.objects.filter(
            (Q(from_user=user) | Q(to_user=user)),
            status=Friendship.ACCEPTED
        ).count()
        Profile.objects.filter(user=user).update(friends_count=count)

    @staticmethod
    def update_followers_count(user):
        """Обновить счетчик подписчиков"""
        count = Friendship.objects.filter(
            to_user=user,
            status=Friendship.REQUESTED
        ).count()
        Profile.objects.filter(user=user).update(followers_count=count)

    @staticmethod
    def send_request(from_user, to_user):
        """Отправить запрос в друзья"""
        if from_user == to_user:
            raise ValueError("You cannot send a request to yourself")

        existing = Friendship.objects.filter(
            from_user=from_user,
            to_user=to_user
        ).first()

        if existing:
            if existing.status == Friendship.REQUESTED:
                raise ValueError("Request already sent")
            elif existing.status == Friendship.ACCEPTED:
                raise ValueError("Already friends")
            elif existing.status == Friendship.REJECTED:
                existing.status = Friendship.REQUESTED
                existing.save()
        else:
            Friendship.objects.create(
                from_user=from_user,
                to_user=to_user,
                status=Friendship.REQUESTED
            )

        FriendshipService.update_followers_count(to_user)

    @staticmethod
    def accept_request(friendship):
        """Принять запрос в друзья"""
        if friendship.status != Friendship.REQUESTED:
            raise ValueError("Only pending requests can be accepted")

        friendship.status = Friendship.ACCEPTED
        friendship.save()

        FriendshipService.update_friends_count(friendship.from_user)
        FriendshipService.update_friends_count(friendship.to_user)
        FriendshipService.update_followers_count(friendship.to_user)

    @staticmethod
    def reject_request(friendship):
        """Отклонить запрос в друзья"""
        if friendship.status != Friendship.REQUESTED:
            raise ValueError("Only pending requests can be rejected")

        friendship.status = Friendship.REJECTED
        friendship.save()

    @staticmethod
    def remove_friendship(user1, user2):
        """Удалить дружбу между пользователями"""
        Friendship.objects.filter(
            (Q(from_user=user1, to_user=user2) |
             Q(from_user=user2, to_user=user1)),
            status=Friendship.ACCEPTED
        ).delete()

        FriendshipService.update_friends_count(user1)
        FriendshipService.update_friends_count(user2)