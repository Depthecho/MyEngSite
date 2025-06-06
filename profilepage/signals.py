from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from django.conf import settings
from typing import Any, Type
from django.db.models import Model
from django.contrib.auth import get_user_model
from .models import Profile, Friendship
from .services import FriendshipService

# Get the actual User model class for proper typing
UserModel: Type[Model] = get_user_model()


@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_user_profile(
        sender: Type[Model],
        instance: Model,
        created: bool,
        **kwargs: Any
) -> None:
    if created:
        # ИСПОЛЬЗУЙТЕ get_or_create ВМЕСТО create
        Profile.objects.get_or_create(user=instance)
        # Возможно, здесь стоит добавить print() для отладки, например:
        # print(f"DEBUG: Profile created/got for user ID: {instance.id}")


# Убедитесь, что этот сигнал закомментирован, пока мы не решим основную проблему:
# @receiver(post_save, sender=settings.AUTH_USER_MODEL)
# def save_user_profile(
#         sender: Type[Model],
#         instance: Model,
#         **kwargs: Any
# ) -> None:
#     if hasattr(instance, 'profile'):
#         instance.profile.save()

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