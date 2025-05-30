from typing import Optional, List, Any, Tuple
from django.db import models
from mainpage.models import CustomUser
from django.db.models.query import QuerySet
from django.db.models.manager import BaseManager
from django.utils import timezone


class Text(models.Model):
    ENGLISH_LEVEL_CHOICES: Tuple[Tuple[str, str], ...] = (
        ('A0', 'A0'),
        ('A1', 'A1'),
        ('A2', 'A2'),
        ('B1', 'B1'),
        ('B2', 'B2'),
        ('C1', 'C1'),
        ('C2', 'C2'),
    )

    added_by: models.ForeignKey[CustomUser] = models.ForeignKey(
        CustomUser,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='texts',
        verbose_name='Added By'
    )
    title: models.CharField = models.CharField(
        max_length=255,
        verbose_name='Title'
    )
    content: models.TextField = models.TextField(
        verbose_name='Content'
    )
    length: models.PositiveIntegerField = models.PositiveIntegerField(
        default=0,
        verbose_name='Length',
        editable=False
    )
    english_level: models.CharField = models.CharField(
        max_length=2,
        choices=ENGLISH_LEVEL_CHOICES,
        verbose_name='English Level'
    )
    created_at: models.DateTimeField = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Created At'
    )

    # Typing for Django model internals
    objects: BaseManager['Text']

    class Meta:
        ordering: Tuple[str, ...] = ('-created_at',)
        verbose_name = 'Text'
        verbose_name_plural = 'Texts'

    def __str__(self) -> str:
        return self.title

    def save(self, *args: Any, **kwargs: Any) -> None:
        # Automatically calculate the length of the text when saving
        self.length = len(self.content)
        super().save(*args, **kwargs)

    @classmethod
    def get_texts_by_level(cls, level: str) -> QuerySet['Text']:
        level_order = ['A0', 'A1', 'A2', 'B1', 'B2', 'C1', 'C2']
        allowed_levels = level_order[:level_order.index(level) + 1]
        return cls.objects.filter(english_level__in=allowed_levels).order_by('-created_at')
