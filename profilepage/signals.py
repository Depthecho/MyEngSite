from django.db.models.signals import post_save
from django.dispatch import receiver
from django.conf import settings
from typing import Any, Type
from django.db.models import Model
from django.contrib.auth import get_user_model
from .models import Profile

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
        Profile.objects.create(
            user=instance,
            username=instance.username,
            email=instance.email,
            first_name='',
            last_name=''
        )


@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def save_user_profile(
        sender: Type[Model],
        instance: Model,
        **kwargs: Any
) -> None:
    if hasattr(instance, 'profile'):
        instance.profile.save()