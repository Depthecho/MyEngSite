from django.db import models
from typing import Optional, List, Any, Tuple
from mainpage.models import CustomUser
from django.db.models.query import QuerySet
from django.db.models.manager import BaseManager


class Card(models.Model):
    user: models.ForeignKey[CustomUser] = models.ForeignKey(
        CustomUser,
        on_delete=models.CASCADE
    )
    user_card_id: models.PositiveIntegerField = models.PositiveIntegerField(
        default=0
    )
    english_word: models.CharField = models.CharField(
        max_length=100
    )
    native_translation: models.CharField = models.CharField(
        max_length=100
    )
    category: models.CharField = models.CharField(
        max_length=50,
        blank=True,
        null=True
    )
    created_at: models.DateTimeField = models.DateTimeField(
        auto_now_add=True
    )

    # Typing for Django model internals
    objects: BaseManager['Card']

    class Meta:
        unique_together: Tuple[str, str] = ('user', 'user_card_id')

    def __str__(self) -> str:
        return f"{self.english_word} -> {self.native_translation}"

    def save(self, *args: Any, **kwargs: Any) -> None:
        if not self.user_card_id:
            last_card: Optional['Card'] = Card.objects.filter(
                user=self.user
            ).order_by('-user_card_id').first()
            self.user_card_id = (last_card.user_card_id + 1) if last_card else 1
        super().save(*args, **kwargs)

    @classmethod
    def get_user_categories(cls, user: CustomUser) -> QuerySet[str]:
        return cls.objects.filter(user=user).exclude(
            category__isnull=True
        ).values_list('category', flat=True).distinct()