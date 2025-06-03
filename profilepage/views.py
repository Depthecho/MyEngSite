from django.contrib import messages
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from django.core.exceptions import PermissionDenied
from django.shortcuts import render, HttpResponseRedirect, get_object_or_404, redirect
from django.http import HttpRequest, HttpResponse
from django.forms import Form
from typing import Any, Dict
from django.urls import reverse
from .services import ProfileService, ProfileUpdateHandler, FriendshipService
from .models import Profile, UserModel, Friendship
from django.db.models import Q

User = get_user_model()


@login_required
def profile_page(request: HttpRequest) -> HttpResponse:
    profile_service: ProfileService = ProfileService(request.user)
    user_profile: Profile = profile_service.get_or_create_profile()
    profile_service.check_achievements()

    return render(request, 'profilepage/profile_page.html', {
        'profile': user_profile,
        'achievements': user_profile.get_achievements()
    })


@login_required
def update_profile(request: HttpRequest) -> HttpResponse:
    handler: ProfileUpdateHandler = ProfileUpdateHandler(request)

    if request.method == 'POST':
        result: Union[Form, HttpResponseRedirect] = handler.process_update()
        if result and not hasattr(result, 'is_valid'):
            return result

    context: Dict[str, Any] = handler.get_forms()
    context['profile'] = request.user.profile

    return render(request, 'profilepage/update_profile.html', context)


@login_required
def public_profile(request, username):
    profile = get_object_or_404(Profile, username=username)

    # Получаем входящий запрос в друзья (если есть)
    incoming_request = None
    if request.user != profile.user:
        try:
            incoming_request = Friendship.objects.get(
                from_user=profile.user,
                to_user=request.user,
                status=Friendship.REQUESTED
            )
        except Friendship.DoesNotExist:
            pass

    context = {
        'profile': profile,
        'friendship': incoming_request,
        'achievements': profile.get_achievements(),
    }

    return render(request, 'profilepage/public_profile.html', context)


def _check_profile_visibility(profile: Profile, viewer: UserModel) -> bool:
    return True


@login_required
def send_friend_request(request, username):
    to_user = get_object_or_404(User, username=username)

    if request.user == to_user:
        messages.error(request, "You cannot send a request to yourself")
        return redirect('public_profile', username=username)

    existing_request = Friendship.objects.filter(
        from_user=request.user,
        to_user=to_user
    ).first()

    if existing_request:
        if existing_request.status == Friendship.REQUESTED:
            messages.info(request, "The request has already been sent")
        elif existing_request.status == Friendship.ACCEPTED:
            messages.info(request, "You are already friends")
        elif existing_request.status == Friendship.REJECTED:
            existing_request.status = Friendship.REQUESTED
            existing_request.save()
            messages.success(request, "Friend request sent")

            FriendshipService.update_followers_count(to_user)
    else:
        Friendship.objects.create(
            from_user=request.user,
            to_user=to_user,
            status=Friendship.REQUESTED
        )
        messages.success(request, "Friend request sent")

        FriendshipService.update_followers_count(to_user)

    return redirect('public_profile', username=username)


@login_required
def accept_friend_request(request, friendship_id):
    friendship = get_object_or_404(
        Friendship,
        id=friendship_id,
        to_user=request.user,
        status=Friendship.REQUESTED
    )

    friendship.status = Friendship.ACCEPTED
    friendship.save()
    messages.success(request, "Friend request accepted")

    FriendshipService.update_friends_count(friendship.from_user)
    FriendshipService.update_friends_count(friendship.to_user)
    FriendshipService.update_followers_count(friendship.to_user)

    return redirect('profile')


@login_required
def reject_friend_request(request, friendship_id):
    friendship = get_object_or_404(
        Friendship,
        id=friendship_id,
        to_user=request.user,
        status=Friendship.REQUESTED
    )

    friendship.status = Friendship.REJECTED
    friendship.save()

    messages.success(request, "Friend request rejected")
    return redirect('profile')
    return redirect('profile')


@login_required
def remove_friend(request, username):
    friend_user = get_object_or_404(User, username=username)

    Friendship.objects.filter(
        Q(from_user=request.user, to_user=friend_user) |
        Q(from_user=friend_user, to_user=request.user),
        status=Friendship.ACCEPTED
    ).delete()

    messages.success(request, f"User {username} has been removed from friends")

    FriendshipService.update_friends_count(request.user)
    FriendshipService.update_friends_count(friend_user)

    return redirect('public_profile', username=username)