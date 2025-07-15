import os
from datetime import datetime
from typing import Any, Dict, List, Optional, Set, Tuple, Type, TypeVar, Union

from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.db import models
from django.conf import settings
from django.contrib.auth import get_user_model
from django.utils import timezone
from django.db.models.signals import post_save
from django.dispatch import receiver


UserModel = get_user_model()

def avatar_upload_path(instance: 'Profile', filename: str) -> str:
    if instance.user and instance.user.id:
        return os.path.join('avatars', str(instance.user.id), filename)
    return os.path.join('avatars', 'default', filename)


class Profile(models.Model):
    user: models.OneToOneField = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='profile',
        verbose_name='User'
    )

    ENGLISH_LEVEL_CHOICES: Tuple[Tuple[str, str], ...] = (
        ('A0', 'Beginner (A0)'),
        ('A1', 'Elementary (A1)'),
        ('A2', 'Pre-Intermediate (A2)'),
        ('B1', 'Intermediate (B1)'),
        ('B2', 'Upper-Intermediate (B2)'),
        ('C1', 'Advanced (C1)'),
        ('C2', 'Proficiency (C2)'),
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
    )
    birth_date: models.DateField = models.DateField(
        null=True,
        blank=True,
        verbose_name='Birth Date'
    )
    study_start_date: models.DateField = models.DateField(
        auto_now_add=True,
        verbose_name='Study Start Date'
    )
    last_visit_date: models.DateField = models.DateField(
        null=True,
        blank=True,
        verbose_name='Last Visit Date'
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
    location: models.CharField = models.CharField(
        max_length=100,
        blank=True,
        verbose_name='Location'
    )

    objects: models.Manager['Profile']

    class Meta:
        verbose_name = 'Profile'
        verbose_name_plural = 'Profiles'

    def __str__(self) -> str:
        return f'{self.user.username} Profile'

    def check_achievements(self) -> None:
        from .models import Achievement

        ACHIEVEMENT_THRESHOLDS = {
            'words': {1: 100, 2: 500, 3: 1500},
            'texts': {1: 50, 2: 150, 3: 500},
            'tests': {1: 50, 2: 150, 3: 500},
        }

        for badge_type, levels in ACHIEVEMENT_THRESHOLDS.items():
            current_value = 0
            if badge_type == 'words':
                current_value = self.words_learned
            elif badge_type == 'texts':
                current_value = self.texts_read
            elif badge_type == 'tests':
                current_value = self.tests_completed

            for level, threshold in sorted(levels.items(), reverse=True):
                if current_value >= threshold:
                    existing_achievement = Achievement.objects.filter(
                        user=self.user,
                        badge_type=badge_type,
                        level=level
                    ).exists()
                    if not existing_achievement:
                        Achievement.objects.create(
                            user=self.user,
                            badge_type=badge_type,
                            level=level,
                            achieved_at=timezone.now()
                        )
                    break

    def get_achievements(self, badge_type: Optional[str] = None) -> models.QuerySet['Achievement']:
        achievements = Achievement.objects.filter(user=self.user)
        if badge_type:
            achievements = achievements.filter(badge_type=badge_type)
        return achievements

    def has_achievement(self, badge_type: str, level: int) -> bool:
        return self.get_achievements(badge_type).filter(level=level).exists()

    def get_friends(self) -> List[UserModel]:
        accepted_friendships = Friendship.objects.filter(
            models.Q(from_user=self.user, status=Friendship.ACCEPTED) |
            models.Q(to_user=self.user, status=Friendship.ACCEPTED)
        ).select_related('from_user', 'to_user')

        friends = []
        for friendship in accepted_friendships:
            if friendship.from_user == self.user:
                friends.append(friendship.to_user)
            else:
                friends.append(friendship.from_user)
        return friends

    def get_pending_requests(self) -> models.QuerySet['Friendship']:
        return Friendship.objects.filter(
            to_user=self.user,
            status=Friendship.REQUESTED
        )

    def get_friendship_status(self, other_user: UserModel) -> str:
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

@receiver(post_save, sender=UserModel)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=UserModel)
def save_user_profile(sender, instance, **kwargs):
    try:
        instance.profile.save()
    except Profile.DoesNotExist:
        Profile.objects.create(user=instance)


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

    user: models.ForeignKey = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        verbose_name='User'
    )
    badge_type: models.CharField = models.CharField(
        max_length=10,
        choices=BADGE_TYPES,
        verbose_name='Badge Type'
    )
    level: models.IntegerField = models.IntegerField(
        choices=LEVELS,
        verbose_name='Level'
    )
    achieved_at: models.DateTimeField = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Achieved At'
    )

    objects: models.Manager['Achievement']

    class Meta:
        ordering: List[str] = ['-achieved_at']
        unique_together = ('user', 'badge_type', 'level')
        verbose_name = 'Achievement'
        verbose_name_plural = 'Achievements'


    def __str__(self) -> str:
        return f"{self.user.username}'s {self.get_level_display()} {self.get_badge_type_display()} Badge"


class Friendship(models.Model):
    REQUESTED = 'requested'
    ACCEPTED = 'accepted'
    REJECTED = 'rejected'

    STATUS_CHOICES = [
        (REQUESTED, 'Requested'),
        (ACCEPTED, 'Accepted'),
        (REJECTED, 'Rejected'),
    ]

    from_user: models.ForeignKey = models.ForeignKey(
        UserModel,
        on_delete=models.CASCADE,
        related_name='friendship_requests_sent',
        verbose_name='From User'
    )
    to_user: models.ForeignKey = models.ForeignKey(
        UserModel,
        on_delete=models.CASCADE,
        related_name='friendship_requests_received',
        verbose_name='To User'
    )
    status: models.CharField = models.CharField(
        max_length=10,
        choices=STATUS_CHOICES,
        default=REQUESTED,
        verbose_name='Status'
    )
    created_at: models.DateTimeField = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Created At'
    )
    updated_at: models.DateTimeField = models.DateTimeField(
        auto_now=True,
        verbose_name='Updated At'
    )
    was_rejected = models.BooleanField(
        default=False
    )

    class Meta:
        unique_together = ('from_user', 'to_user')
        ordering = ['-created_at']
        verbose_name = 'Friendship'
        verbose_name_plural = 'Friendships'

    def __str__(self) -> str:
        return f"{self.from_user.username} -> {self.to_user.username} ({self.get_status_display()})"


class Notification(models.Model):
    NOTIFICATION_TYPES: Tuple[Tuple[str, str], ...] = (
        ('FRIEND_REQUEST', 'Friend Request'),
        ('SYSTEM', 'System Notification'),
        ('ACHIEVEMENT', 'Achievement Unlocked'),
    )

    user: models.ForeignKey = models.ForeignKey(
        UserModel,
        on_delete=models.CASCADE,
        related_name='notifications',
        verbose_name='User'
    )
    notification_type: models.CharField = models.CharField(
        max_length=20,
        choices=NOTIFICATION_TYPES,
        verbose_name='Notification Type'
    )
    title: models.CharField = models.CharField(
        max_length=100,
        verbose_name='Title'
    )
    message: models.TextField = models.TextField(
        verbose_name='Message'
    )
    is_read: models.BooleanField = models.BooleanField(
        default=False,
        verbose_name='Is Read'
    )
    created_at: models.DateTimeField = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Created At'
    )
    content_type: models.ForeignKey = models.ForeignKey(
        ContentType,
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        verbose_name='Content Type'
    )
    object_id: models.PositiveIntegerField = models.PositiveIntegerField(
        null=True,
        blank=True,
        verbose_name='Object ID'
    )
    content_object: GenericForeignKey = GenericForeignKey('content_type', 'object_id')

    class Meta:
        ordering = ['-created_at']
        verbose_name = 'Notification'
        verbose_name_plural = 'Notifications'

    def __str__(self) -> str:
        return f"{self.get_notification_type_display()} for {self.user.username} at {self.created_at.strftime('%Y-%m-%d %H:%M')}"