from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager
from django.contrib.auth.models import PermissionsMixin, Group, Permission
from django.db import models
from django.utils import timezone
from typing import Any, Dict, Optional, Set
from django.db.models.manager import BaseManager
from django.db.models.query import QuerySet


class CustomUserManager(BaseUserManager):
    def create_user(
        self,
        username: str,
        email: str,
        password: Optional[str] = None,
        **extra_fields: Dict[str, Any]
    ) -> 'CustomUser':
        """
        Creates and saves a User with the given username, email and password.
        """
        if not email:
            raise ValueError('The Email field must be set')
        email = self.normalize_email(email)
        user: 'CustomUser' = self.model(
            username=username,
            email=email,
            **extra_fields
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(
        self,
        username: str,
        email: str,
        password: Optional[str] = None,
        **extra_fields: Dict[str, Any]
    ) -> 'CustomUser':
        """
        Creates and saves a superuser with the given username, email and password.
        """
        extra_fields.update({
            'is_staff': True,
            'is_superuser': True,
            'is_active': True,
        })
        return self.create_user(username, email, password, **extra_fields)


class CustomUser(AbstractBaseUser, PermissionsMixin):
    username: models.CharField = models.CharField(
        max_length=150,
        unique=True,
        db_index=True,
        null=False
    )
    email: models.EmailField = models.EmailField(
        unique=True,
        null=False
    )
    first_name: models.CharField = models.CharField(
        max_length=30,
        blank=True,
        null=True
    )
    last_name: models.CharField = models.CharField(
        max_length=150,
        blank=True,
        null=True
    )
    is_active: models.BooleanField = models.BooleanField(
        default=True
    )
    is_staff: models.BooleanField = models.BooleanField(
        default=False
    )
    date_joined: models.DateTimeField = models.DateTimeField(
        default=timezone.now
    )
    last_login: models.DateTimeField = models.DateTimeField(
        null=True,
        blank=True
    )

    groups: models.ManyToManyField = models.ManyToManyField(
        Group,
        verbose_name='groups',
        blank=True,
        help_text='The groups this user belongs to.',
        related_name='customuser_set',
        related_query_name='customuser',
    )
    user_permissions: models.ManyToManyField = models.ManyToManyField(
        Permission,
        verbose_name='user permissions',
        blank=True,
        help_text='Specific permissions for this user.',
        related_name='customuser_set',
        related_query_name='customuser',
    )

    objects: BaseManager['CustomUser'] = CustomUserManager()

    USERNAME_FIELD: str = 'username'
    REQUIRED_FIELDS: list[str] = ['email']

    def delete(self, *args: Any, **kwargs: Any) -> None:
        """Delete user and associated profile if exists."""
        profile = getattr(self, 'profile', None)
        if profile:
            profile.delete()
        super().delete(*args, **kwargs)

    def __str__(self) -> str:
        return self.username

    class Meta:
        verbose_name: str = 'user'
        verbose_name_plural: str = 'users'