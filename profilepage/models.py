import os
from datetime import datetime
from typing import Any, Dict, List, Optional, Set, Tuple, Type, TypeVar, Union
from django.db import models
from django.conf import settings
from django.contrib.auth import get_user_model
from django.utils import timezone

UserModel = get_user_model()

def avatar_upload_path(instance: 'Profile', filename: str) -> str:
    """Generate upload path for user avatars."""
    return os.path.join('avatars', str(instance.user.id), filename)


class Profile(models.Model):
    user: models.OneToOneField[UserModel] = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='profile'
    )
    username: models.CharField = models.CharField(
        max_length=150,
        verbose_name='Username'
    )
    email: models.EmailField = models.EmailField(
        verbose_name='Email'
    )
    first_name: models.CharField = models.CharField(
        max_length=30,
        verbose_name='First Name'
    )
    last_name: models.CharField = models.CharField(
        max_length=150,
        verbose_name='Last Name'
    )

    ENGLISH_LEVEL_CHOICES: Tuple[Tuple[str, str], ...] = (
        ('A0', 'A0'),
        ('A1', 'A1'),
        ('A2', 'A2'),
        ('B1', 'B1'),
        ('B2', 'B2'),
        ('C1', 'C1'),
        ('C2', 'C2'),
    )
    english_level: models.CharField = models.CharField(
        max_length=2,
        choices=ENGLISH_LEVEL_CHOICES,
        default='A0',
        verbose_name='English Level'
    )

    words_learned: models.PositiveIntegerField = models.PositiveIntegerField(
        default=0,
        verbose_name='Words Learned'
    )
    texts_read: models.PositiveIntegerField = models.PositiveIntegerField(
        default=0,
        verbose_name='Texts Read'
    )
    tests_completed: models.PositiveIntegerField = models.PositiveIntegerField(
        default=0,
        verbose_name='Tests Completed'
    )
    streak: models.PositiveIntegerField = models.PositiveIntegerField(
        default=0,
        verbose_name='Current Streak'
    )
    friends_count: models.PositiveIntegerField = models.PositiveIntegerField(
        default=0,
        verbose_name='Friends Count'
    )
    followers_count: models.PositiveIntegerField = models.PositiveIntegerField(
        default=0,
        verbose_name='Followers Count'
    )
    avatar: models.ImageField = models.ImageField(
        upload_to=avatar_upload_path,
        default='avatars/default_user.png',
        verbose_name='Avatar'
    )
    birth_date: models.DateField = models.DateField(
        null=True,
        blank=True,
        verbose_name='Birth Date'
    )
    study_start_date: models.DateField = models.DateField(
        auto_now_add=True,
        verbose_name='Study Start Date',
        blank=True
    )
    hide_first_name: models.BooleanField = models.BooleanField(
        default=False,
        verbose_name='Hide First Name'
    )
    hide_last_name: models.BooleanField = models.BooleanField(
        default=False,
        verbose_name='Hide Last Name'
    )
    hide_birth_date: models.BooleanField = models.BooleanField(
        default=False,
        verbose_name='Hide Birth Date'
    )
    bio: models.TextField = models.TextField(
        max_length=500,
        blank=True,
        verbose_name='Biography'
    )
    website: models.URLField = models.URLField(
        blank=True,
        verbose_name='Website'
    )
    location: models.CharField = models.CharField(
        max_length=100,
        blank=True,
        verbose_name='Location'
    )

    objects: models.Manager['Profile']

    def __str__(self) -> str:
        return f'{self.username} Profile'

    def check_achievements(self) -> bool:
        """Check and assign achievements based on user progress."""
        from .models import Achievement

        # Words achievements
        if self.words_learned >= 1500:
            Achievement.objects.get_or_create(
                user=self.user,
                badge_type='words',
                level=3,
                defaults={'achieved_at': timezone.now()}
            )
        elif self.words_learned >= 500:
            Achievement.objects.get_or_create(
                user=self.user,
                badge_type='words',
                level=2,
                defaults={'achieved_at': timezone.now()}
            )
        elif self.words_learned >= 100:
            Achievement.objects.get_or_create(
                user=self.user,
                badge_type='words',
                level=1,
                defaults={'achieved_at': timezone.now()}
            )

        # Texts achievements
        if self.texts_read >= 500:
            Achievement.objects.get_or_create(
                user=self.user,
                badge_type='texts',
                level=3,
                defaults={'achieved_at': timezone.now()}
            )
        elif self.texts_read >= 150:
            Achievement.objects.get_or_create(
                user=self.user,
                badge_type='texts',
                level=2,
                defaults={'achieved_at': timezone.now()}
            )
        elif self.texts_read >= 50:
            Achievement.objects.get_or_create(
                user=self.user,
                badge_type='texts',
                level=1,
                defaults={'achieved_at': timezone.now()}
            )

        # Tests achievements
        if self.tests_completed >= 500:
            Achievement.objects.get_or_create(
                user=self.user,
                badge_type='tests',
                level=3,
                defaults={'achieved_at': timezone.now()}
            )
        elif self.tests_completed >= 150:
            Achievement.objects.get_or_create(
                user=self.user,
                badge_type='tests',
                level=2,
                defaults={'achieved_at': timezone.now()}
            )
        elif self.tests_completed >= 50:
            Achievement.objects.get_or_create(
                user=self.user,
                badge_type='tests',
                level=1,
                defaults={'achieved_at': timezone.now()}
            )

        return True

    def get_achievements(self, badge_type: Optional[str] = None) -> models.QuerySet['Achievement']:
        """Get all achievements for this user, optionally filtered by badge type."""
        achievements = Achievement.objects.filter(user=self.user)
        if badge_type:
            achievements = achievements.filter(badge_type=badge_type)
        return achievements

    def has_achievement(self, badge_type: str, level: int) -> bool:
        """Check if user has a specific achievement."""
        return self.get_achievements(badge_type).filter(level=level).exists()

    def get_friends(self):
        """Возвращает список друзей пользователя"""
        accepted = Friendship.objects.filter(
            models.Q(from_user=self.user, status=Friendship.ACCEPTED) |
            models.Q(to_user=self.user, status=Friendship.ACCEPTED)
        )

        friends = []
        for friendship in accepted:
            if friendship.from_user == self.user:
                friends.append(friendship.to_user)
            else:
                friends.append(friendship.from_user)
        return friends

    def get_pending_requests(self):
        """Возвращает входящие заявки в друзья"""
        return Friendship.objects.filter(
            to_user=self.user,
            status=Friendship.REQUESTED
        )

    def get_friendship_status(self, other_user):
        """Возвращает статус дружбы между пользователями"""
        if self.user == other_user:
            return 'self'

        try:
            friendship = Friendship.objects.get(
                from_user=self.user,
                to_user=other_user
            )
            return friendship.status
        except Friendship.DoesNotExist:
            try:
                friendship = Friendship.objects.get(
                    from_user=other_user,
                    to_user=self.user
                )
                if friendship.status == Friendship.REQUESTED:
                    return 'request_received'
                return friendship.status
            except Friendship.DoesNotExist:
                return 'none'


class Achievement(models.Model):
    BADGE_TYPES: Tuple[Tuple[str, str], ...] = (
        ('words', 'Words'),
        ('texts', 'Texts'),
        ('tests', 'Tests'),
    )
    LEVELS: Tuple[Tuple[int, str], ...] = (
        (1, 'Bronze'),
        (2, 'Silver'),
        (3, 'Gold'),
    )

    user: models.ForeignKey[UserModel] = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE
    )
    badge_type: models.CharField = models.CharField(
        max_length=10,
        choices=BADGE_TYPES
    )
    level: models.IntegerField = models.IntegerField(
        choices=LEVELS
    )
    achieved_at: models.DateTimeField = models.DateTimeField(
        auto_now_add=True
    )

    objects: models.Manager['Achievement']

    class Meta:
        ordering: List[str] = ['-achieved_at']

    def __str__(self) -> str:
        return f"{self.get_badge_type_display()} {self.get_level_display()} Badge"


class Friendship(models.Model):
    REQUESTED = 'requested'
    ACCEPTED = 'accepted'
    REJECTED = 'rejected'

    STATUS_CHOICES = [
        (REQUESTED, 'Requested'),
        (ACCEPTED, 'Accepted'),
        (REJECTED, 'Rejected'),
    ]

    from_user = models.ForeignKey(
        UserModel,
        on_delete=models.CASCADE,
        related_name='friendship_requests_sent',

    )
    to_user = models.ForeignKey(
        UserModel,
        on_delete=models.CASCADE,
        related_name='friendship_requests_received',
    )
    status = models.CharField(
        max_length=10,
        choices=STATUS_CHOICES,
        default=REQUESTED
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        unique_together = ('from_user', 'to_user')
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.from_user} → {self.to_user} ({self.status})"