from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from .models import Card
from profilepage.models import Profile

def update_words_learned(user):
    profile = getattr(user, 'profile', None)
    if profile:
        profile.words_learned = Card.objects.filter(user=user).count()
        profile.save(update_fields=['words_learned'])

@receiver(post_save, sender=Card)
def card_saved(sender, instance, created, **kwargs):
    if created:
        update_words_learned(instance.user)

@receiver(post_delete, sender=Card)
def card_deleted(sender, instance, **kwargs):
    update_words_learned(instance.user)
