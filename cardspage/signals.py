from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from typing import Any, Optional
from .models import Card
from profilepage.models import Profile
from django.contrib.auth import get_user_model
from django.db.models.query import QuerySet

UserModel = get_user_model()


def update_words_learned(user: UserModel) -> None:
    profile: Optional[Profile] = getattr(user, 'profile', None)
    if profile:
        count: int = Card.objects.filter(user=user).count()
        profile.words_learned = count
        profile.save(update_fields=['words_learned'])


@receiver(post_save, sender=Card)
def card_saved(
        sender: Any,
        instance: Card,
        created: bool,
        **kwargs: Any
) -> None:
    if created:
        update_words_learned(instance.user)


@receiver(post_delete, sender=Card)
def card_deleted(
        sender: Any,
        instance: Card,
        **kwargs: Any
) -> None:
    update_words_learned(instance.user)