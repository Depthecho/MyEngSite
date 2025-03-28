import os
from django.db import models
from django.conf import settings

def avatar_upload_path(instance, filename):
    return os.path.join('avatars', str(instance.user.id), filename)

class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='profile')
    username = models.CharField(max_length=150, verbose_name='Username')
    email = models.EmailField(verbose_name='Email')
    first_name = models.CharField(max_length=30, verbose_name='First Name')
    last_name = models.CharField(max_length=150, verbose_name='Last Name')
    words_learned = models.PositiveIntegerField(default=0, verbose_name='Words Learned')
    texts_read = models.PositiveIntegerField(default=0, verbose_name='Texts Read')
    tests_completed = models.PositiveIntegerField(default=0, verbose_name='Tests Completed')
    streak = models.PositiveIntegerField(default=0, verbose_name='Current Streak')
    friends_count = models.PositiveIntegerField(default=0, verbose_name='Friends Count')
    followers_count = models.PositiveIntegerField(default=0, verbose_name='Followers Count')
    avatar = models.ImageField(
        upload_to=avatar_upload_path,
        default='avatars/default_user.png',
        verbose_name='Avatar'
    )

    def __str__(self):
        return f'{self.username} Profile'

    def check_achievements(self):
        from django.utils import timezone
        from .models import Achievement

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




class Achievement(models.Model):
    BADGE_TYPES = (
        ('words', 'Words'),
        ('texts', 'Texts'),
        ('tests', 'Tests'),
    )
    LEVELS = (
        (1, 'Bronze'),
        (2, 'Silver'),
        (3, 'Gold'),
    )
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    badge_type = models.CharField(max_length=10, choices=BADGE_TYPES)
    level = models.IntegerField(choices=LEVELS)
    achieved_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-achieved_at']

    def __str__(self):
        return f"{self.get_badge_type_display()} {self.get_level_display()} Badge"