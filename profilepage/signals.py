from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from django.conf import settings
from typing import Any, Type
from django.db.models import Model
from django.contrib.auth import get_user_model
from .models import Profile, Friendship
from .services import FriendshipService

UserModel: Type[Model] = get_user_model()


@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_user_profile(
        sender: Type[Model],
        instance: Model,
        created: bool,
        **kwargs: Any
) -> None:
    if created:
        Profile.objects.get_or_create(user=instance)

@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def save_user_profile(
         sender: Type[Model],
         instance: Model,
         **kwargs: Any
 ) -> None:
     if hasattr(instance, 'profile'):
         instance.profile.save()

@receiver(post_save, sender=Friendship)
def update_counts_on_friendship_change(sender, instance, **kwargs):
    if instance.status == Friendship.ACCEPTED:
        FriendshipService.update_friends_count(instance.from_user)
        FriendshipService.update_friends_count(instance.to_user)
        FriendshipService.update_followers_count(instance.to_user)

@receiver(post_delete, sender=Friendship)
def update_counts_on_friendship_delete(sender, instance, **kwargs):
    FriendshipService.update_friends_count(instance.from_user)
    FriendshipService.update_friends_count(instance.to_user)
    FriendshipService.update_followers_count(instance.to_user)