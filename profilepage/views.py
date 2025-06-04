from django.contrib import messages
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from django.contrib.contenttypes.models import ContentType
from django.core.exceptions import PermissionDenied
from django.core.paginator import Paginator
from django.shortcuts import render, HttpResponseRedirect, get_object_or_404, redirect
from django.http import HttpRequest, HttpResponse, JsonResponse
from django.forms import Form
from typing import Any, Dict
from django.urls import reverse
from django.views.decorators.http import require_POST

from .services import ProfileService, ProfileUpdateHandler, FriendshipService, NotificationService
from .models import Profile, UserModel, Friendship, Notification
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
@login_required
def accept_friend_request(request, friendship_id):
    try:
        friendship = get_object_or_404(
            Friendship,
            id=friendship_id,
            to_user=request.user,
            status=Friendship.REQUESTED
        )
        FriendshipService.accept_request(friendship)
        messages.success(request, "Friend request accepted")

        friendship_content_type = ContentType.objects.get_for_model(Friendship)

        notification_for_friendship = Notification.objects.filter(
            user=request.user,
            notification_type='FRIEND_REQUEST',
            content_type=friendship_content_type,
            object_id=friendship.id,
            is_read=False
        ).first()

        if notification_for_friendship:
            NotificationService.mark_as_read(notification_for_friendship.id, request.user)

    except ValueError as e:
        messages.error(request, str(e))

    if request.headers.get('x-requested-with') == 'XMLHttpRequest':
        unread_count = NotificationService.get_unread_count(request.user)
        return JsonResponse({'status': 'success', 'unread_count': unread_count})

    return redirect('profile')


@login_required
def reject_friend_request(request, friendship_id):
    try:
        friendship = get_object_or_404(
            Friendship,
            id=friendship_id,
            to_user=request.user,
            status=Friendship.REQUESTED
        )
        FriendshipService.reject_request(friendship)
        messages.success(request, "Friend request rejected")

        friendship_content_type = ContentType.objects.get_for_model(Friendship)
        notification_for_friendship = Notification.objects.filter(
            user=request.user,
            notification_type='FRIEND_REQUEST',
            content_type=friendship_content_type,
            object_id=friendship.id,
            is_read=False
        ).first()

        if notification_for_friendship:
            NotificationService.mark_as_read(notification_for_friendship.id, request.user)


    except ValueError as e:
        messages.error(request, str(e))

    if request.headers.get('x-requested-with') == 'XMLHttpRequest':
        unread_count = NotificationService.get_unread_count(request.user)
        return JsonResponse({'status': 'success', 'unread_count': unread_count})

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


@login_required
def friends_list(request):
    friends = FriendshipService.get_friends(request.user)
    paginator = Paginator(friends, 20)
    return render(request, 'profilepage/friends_list.html', {
        'page_obj': paginator.get_page(request.GET.get('page')),
        'friends_count': len(friends)
    })


@login_required
def followers_list(request):
    followers = FriendshipService.get_followers(request.user)
    paginator = Paginator(followers, 20)
    return render(request, 'profilepage/followers_list.html', {
        'page_obj': paginator.get_page(request.GET.get('page')),
        'followers_count': followers.count()
    })


@login_required
def send_friend_request(request, username):
    try:
        to_user = get_object_or_404(User, username=username)
        FriendshipService.send_request(request.user, to_user)
        messages.success(request, "Friend request sent")
    except ValueError as e:
        messages.error(request, str(e))

    return redirect('public_profile', username=username)


@login_required
@require_POST
def accept_friend_request(request: HttpRequest, friendship_id: int) -> JsonResponse:
    if request.method == 'POST':
        try:
            friendship = get_object_or_404(
                Friendship,
                id=friendship_id,
                to_user=request.user,
                status=Friendship.REQUESTED
            )
            FriendshipService.accept_request(friendship)
            messages.success(request, "Friend request accepted")

            friendship_content_type = ContentType.objects.get_for_model(Friendship)
            notification_for_friendship = Notification.objects.filter(
                user=request.user,
                notification_type='FRIEND_REQUEST',
                content_type=friendship_content_type,
                object_id=friendship.id,
                is_read=False
            ).first()

            if notification_for_friendship:
                notification_for_friendship.delete()

            unread_count = NotificationService.get_unread_count(request.user)
            return JsonResponse({
                'status': 'success',
                'unread_count': unread_count,
            })

        except ValueError as e:
            messages.error(request, str(e))
            return JsonResponse({'status': 'error', 'message': str(e)}, status=400)

    return JsonResponse({'status': 'error', 'message': 'Invalid request method'}, status=405)




@login_required
def reject_friend_request(request: HttpRequest, friendship_id: int) -> JsonResponse:
    if request.method == 'POST':
        try:
            friendship = get_object_or_404(
                Friendship,
                id=friendship_id,
                to_user=request.user,
                status=Friendship.REQUESTED
            )
            FriendshipService.reject_request(friendship)
            messages.success(request, "Friend request rejected")

            # Находим уведомление, связанное с этим запросом дружбы
            friendship_content_type = ContentType.objects.get_for_model(Friendship)
            notification_for_friendship = Notification.objects.filter(
                user=request.user,
                notification_type='FRIEND_REQUEST',
                content_type=friendship_content_type,
                object_id=friendship.id,
                is_read=False
            ).first()

            if notification_for_friendship:
                # ИЗМЕНЕНИЕ ЗДЕСЬ: УДАЛЯЕМ УВЕДОМЛЕНИЕ ИЗ БД
                notification_for_friendship.delete()

            # Возвращаем JsonResponse с обновленным счетчиком для AJAX
            unread_count = NotificationService.get_unread_count(request.user)
            return JsonResponse({
                'status': 'success',
                'unread_count': unread_count,
            })

        except ValueError as e:
            messages.error(request, str(e))
            return JsonResponse({'status': 'error', 'message': str(e)}, status=400)

    return JsonResponse({'status': 'error', 'message': 'Invalid request method'}, status=405)


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
        # ИЗМЕНЕНИЕ ЗДЕСЬ: Вызываем метод delete() ORM
        notification.delete() # <--- ЭТО УДАЛИТ УВЕДОМЛЕНИЕ ИЗ БАЗЫ ДАННЫХ

        unread_count = NotificationService.get_unread_count(request.user)
        return JsonResponse({'status': 'success', 'unread_count': unread_count})
    except Notification.DoesNotExist:
        return JsonResponse({'status': 'error', 'message': 'Notification not found or you do not have permission to delete it.'}, status=404)
    except Exception as e:
        return JsonResponse({'status': 'error', 'message': str(e)}, status=500)