import random
from django.db import models
from django.conf import settings
from django.utils import timezone
from typing import Optional


class ChatManager(models.Manager):
    def generate_unique_chat_id(self):
        """Генерирует уникальный 9-значный ID чата"""
        while True:
            chat_id = random.randint(100_000_000, 999_999_999)  # 9 цифр
            if not self.filter(id=chat_id).exists():
                return chat_id


class Chat(models.Model):
    objects = ChatManager()

    id = models.BigIntegerField(
        primary_key=True,
        editable=False,
        unique=True,
        verbose_name='Chat ID'
    )

    participants = models.ManyToManyField(
        settings.AUTH_USER_MODEL,
        related_name='chats',
        verbose_name='Participants'
    )

    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Created At'
    )

    updated_at = models.DateTimeField(
        auto_now=True,
        verbose_name='Last Updated At'
    )

    class Meta:
        verbose_name = 'Chat'
        verbose_name_plural = 'Chats'
        ordering = ['-updated_at']

    def save(self, *args, **kwargs):
        if not self.id:
            self.id = self.__class__.objects.generate_unique_chat_id()
        super().save(*args, **kwargs)

    def __str__(self) -> str:
        participant_names = ", ".join([user.username for user in self.participants.all()])
        return f"Chat {self.id} with {participant_names}"

    @property
    def get_last_message(self) -> Optional['Message']:
        return self.messages.order_by('-timestamp').first()

    def unread_messages_count(self, user) -> int:
        """Количество непрочитанных сообщений для конкретного пользователя"""
        return self.messages.filter(is_read=False).exclude(sender=user).count()


class Message(models.Model):
    chat = models.ForeignKey(
        Chat,
        on_delete=models.CASCADE,
        related_name='messages',
        verbose_name='Chat'
    )

    sender = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='sent_messages',
        verbose_name='Sender'
    )

    content = models.TextField(
        verbose_name='Message Content'
    )

    timestamp = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Timestamp'
    )

    is_read = models.BooleanField(
        default=False,
        verbose_name='Is Read'
    )

    class Meta:
        verbose_name = 'Message'
        verbose_name_plural = 'Messages'
        ordering = ['timestamp']
        indexes = [
            models.Index(fields=['timestamp']),
        ]

    def __str__(self) -> str:
        return f"Message {self.id} from {self.sender.username} in chat {self.chat.id}"