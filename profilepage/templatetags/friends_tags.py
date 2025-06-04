from django import template
from ..models import Friendship
from ..services import FriendshipService
from django.db.models import Q

register = template.Library()

@register.simple_tag(takes_context=True)
def friendship_status(context, user1, user2):
    if not user1.is_authenticated or user1 == user2:
        return 'self_or_not_authenticated'

    are_friends = Friendship.objects.filter(
        (Q(from_user=user1, to_user=user2, status=Friendship.ACCEPTED) |
         Q(from_user=user2, to_user=user1, status=Friendship.ACCEPTED))
    ).exists()
    if are_friends:
        return 'friends'

    request_sent = Friendship.objects.filter(
        from_user=user1, to_user=user2, status=Friendship.REQUESTED
    ).exists()
    if request_sent:
        return 'request_sent'

    request_received = Friendship.objects.filter(
        from_user=user2, to_user=user1, status=Friendship.REQUESTED
    ).exists()
    if request_received:
        return 'request_received'

    return 'not_friends'

@register.filter
def pending_requests(user):
    return user.profile.get_pending_requests()

@register.simple_tag
def update_friends_count(user):
    FriendshipService.update_friends_count(user)
    return ""

@register.simple_tag
def update_followers_count(user):
    FriendshipService.update_followers_count(user)
    return ""