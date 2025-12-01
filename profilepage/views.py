from django.conf import settings
from django.contrib import messages
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from django.contrib.contenttypes.models import ContentType
from django.core.exceptions import PermissionDenied
from django.core.paginator import Paginator
from django.shortcuts import render, HttpResponseRedirect, get_object_or_404, redirect
from django.http import HttpRequest, HttpResponse, JsonResponse
from django.forms import Form
from typing import Any, Dict, Union
from django.urls import reverse
from django.views.decorators.http import require_POST
from .services import ProfileService, ProfileUpdateHandler, FriendshipService, NotificationService
from .models import Profile, UserModel, Friendship, Notification
from django.db.models import Q
from textspage.models import Text

User = get_user_model()


@login_required
def profile_page(request: HttpRequest) -> HttpResponse:
    profile_service: ProfileService = ProfileService(request.user)
    user_profile: Profile = profile_service.get_or_create_profile()
    profile_service.check_achievements()

    texts_read = Text.objects.filter(read_by=request.user).count()
    user_profile.texts_read = texts_read
    user_profile.save()

    return render(request, 'profilepage/profile_page.html', {
        'profile': user_profile,
        'achievements': user_profile.get_achievements(),
        'LANGUAGES': settings.LANGUAGES,
        'texts_read': texts_read,
    })

@login_required
def update_profile(request: HttpRequest) -> HttpResponse:
    handler = ProfileUpdateHandler(request)

    if request.method == 'POST':
        response = handler.process_update()
        if response:
            return response

    return render(request, 'profilepage/update_profile.html', {
        **handler.get_context(),
        'profile': request.user.profile,
        'LANGUAGES': settings.LANGUAGES,
    })


@login_required
def public_profile(request, username):
    profile_owner = get_object_or_404(User, username=username)
    profile = get_object_or_404(Profile, user=profile_owner)

    status = request.user.profile.get_friendship_status(profile_owner)

    incoming_request = None
    if status == 'request_received':
        incoming_request = Friendship.objects.filter(
            from_user=profile_owner,
            to_user=request.user,
            status=Friendship.REQUESTED
        ).first()

    context = {
        'profile': profile,
        'status': status,
        'incoming_request': incoming_request,
        'achievements': profile.get_achievements(),
        'LANGUAGES': settings.LANGUAGES,
    }

    return render(request, 'profilepage/public_profile.html', context)


def _check_profile_visibility(profile: Profile, viewer: UserModel) -> bool:
    return True

@login_required
def reject_friend_request(request: HttpRequest, friendship_id: int) -> HttpResponse:
    if request.method == 'POST':
        try:
            friendship = get_object_or_404(
                Friendship,
                id=friendship_id,
                to_user=request.user,
                status=Friendship.REQUESTED
            )
            FriendshipService.reject_request(friendship)
            messages.success(request, "Friend request rejected. 😔")

            notification_for_friendship = Notification.objects.filter(
                user=request.user,
                notification_type='FRIEND_REQUEST',
                content_type=ContentType.objects.get_for_model(Friendship),
                object_id=friendship.id,
                is_read=False
            ).first()

            if notification_for_friendship:
                notification_for_friendship.delete()

            return redirect('followers_list')

        except ValueError as e:
            messages.error(request, str(e))
        except Exception as e:
            messages.error(request, f"An unexpected error occurred: {e}")

    return redirect('followers_list')


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


@login_required
def friends_list(request):
    friends = FriendshipService.get_friends(request.user)
    paginator = Paginator(friends, 20)
    return render(request, 'profilepage/friends_list.html', {
        'page_obj': paginator.get_page(request.GET.get('page')),
        'friends_count': len(friends),
        'LANGUAGES': settings.LANGUAGES,
    })


@login_required
def followers_list(request):
    incoming_requests_qs = Friendship.objects.filter(
        Q(to_user=request.user, status=Friendship.REQUESTED) |
        Q(to_user=request.user, status=Friendship.REJECTED, was_rejected=True)
    ).select_related('from_user__profile').order_by('-created_at')

    followers_data = []
    for req in incoming_requests_qs:
        followers_data.append({
            'follower': req.from_user,
            'friendship_request': req
        })

    followers_count = len(followers_data)

    paginator = Paginator(followers_data, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        'page_obj': page_obj,
        'followers_count': followers_count,
        'LANGUAGES': settings.LANGUAGES,
    }
    return render(request, 'profilepage/followers_list.html', context)


@login_required
def send_friend_request(request, username):
    try:
        to_user = get_object_or_404(User, username=username)
        FriendshipService.send_request(request.user, to_user)
        messages.success(request, "Friend request sent")
    except ValueError as e:
        messages.error(request, str(e))

    return redirect('followers_list')


@login_required
@require_POST
def accept_friend_request(request: HttpRequest, friendship_id: int) -> HttpResponse:
    if request.method == 'POST':
        try:
            friendship = get_object_or_404(
                Friendship,
                id=friendship_id,
                to_user=request.user,
                status=Friendship.REQUESTED
            )
            FriendshipService.accept_request(friendship)
            messages.success(request, "Friend request accepted! 🎉")

            notification_for_friendship = Notification.objects.filter(
                user=request.user,
                notification_type='FRIEND_REQUEST',
                content_type=ContentType.objects.get_for_model(Friendship),
                object_id=friendship.id,
                is_read=False
            ).first()

            if notification_for_friendship:
                notification_for_friendship.delete()

            return redirect('friends_list')

        except ValueError as e:
            messages.error(request, str(e))
        except Exception as e:
            messages.error(request, f"An unexpected error occurred: {e}")

    return redirect('followers_list')

@login_required
def add_from_rejected(request: HttpRequest, friendship_id: int) -> HttpRequest:
    if request.method == 'POST':
        try:
            friendship = get_object_or_404(
                Friendship,
                id=friendship_id,
                to_user=request.user,
                status=Friendship.REJECTED,
                was_rejected=True
            )

            FriendshipService.accept_rejected_request(friendship)

            NotificationService.create_notification(
                user=friendship.from_user,
                notification_type='FRIEND_REQUEST',
                title='Friend Request Accepted',
                message=f'{request.user.username} has accepted your friend request.',
                related_object=friendship
            )

            messages.success(request, f"{friendship.from_user.username} is now your friend!")
            return redirect('friends_list')

        except Friendship.DoesNotExist:
            messages.error(request, "Friendship request not found or cannot be accepted.")
            return redirect('followers_list')
        except ValueError as e:
            messages.error(request, str(e))
            return redirect('followers_list')
        except Exception as e:
            messages.error(request, f"An unexpected error occurred: {e}")
            return redirect('followers_list')
    else:
        return redirect('followers_list')

@login_required
def remove_friend(request, username):
    try:
        friend_user = get_object_or_404(User, username=username)
        FriendshipService.remove_friendship(request.user, friend_user)
        messages.success(request, f"User {username} removed from friends")
    except Exception as e:
        messages.error(request, str(e))

    return redirect('public_profile', username=username)

@login_required
def mark_all_notifications_as_read(request):
    if request.method == 'POST':
        request.user.notifications.filter(is_read=False).update(is_read=True)
        return JsonResponse({'status': 'success'})
    return JsonResponse({'status': 'error'}, status=400)

@login_required
@require_POST
def delete_notification(request, notification_id):
    try:
        notification = Notification.objects.get(id=notification_id, user=request.user)
        notification.delete()

        unread_count = NotificationService.get_unread_count(request.user)
        return JsonResponse({'status': 'success', 'unread_count': unread_count})
    except Notification.DoesNotExist:
        return JsonResponse({'status': 'error', 'message': 'Notification not found or you do not have permission to delete it.'}, status=404)
    except Exception as e:
        return JsonResponse({'status': 'error', 'message': str(e)}, status=500)