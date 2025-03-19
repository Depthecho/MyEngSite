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
    avatar = models.ImageField(
        upload_to=avatar_upload_path,
        default='avatars/default_user.png',
        verbose_name='Avatar'
    )

    def __str__(self):
        return f'{self.username} Profile'