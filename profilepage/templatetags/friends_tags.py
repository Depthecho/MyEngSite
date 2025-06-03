from django import template
from ..models import Friendship
from ..services import FriendshipService

register = template.Library()

@register.simple_tag
def friendship_status(from_user, to_user):
    return from_user.profile.get_friendship_status(to_user)

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