from django.db import models
from django.conf import settings
from django.utils import timezone
from django.db.models import Q
from typing import Any, Dict, List, Optional, Set, Tuple, Type, TypeVar, Union


class Chat(models.Model):
    participants: models.ManyToManyField = models.ManyToManyField(
        settings.AUTH_USER_MODEL,
        related_name='chats',
        verbose_name='Participants'
    )
    created_at: models.DateTimeField = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Created At'
    )
    updated_at: models.DateTimeField = models.DateTimeField(
        auto_now=True,
        verbose_name='Last Updated At'
    )

    class Meta:
        verbose_name: str = 'Chat'
        verbose_name_plural: str = 'Chats'
        ordering: List[str] = ['-updated_at']

    def __str__(self) -> str:
        participant_names = ", ".join([user.username for user in self.participants.all()])
        return f"Chat with {participant_names}"

    @property
    def get_last_message(self) -> Optional['Message']:
        return self.messages.order_by('-timestamp').first()

    @property
    def unread_messages_count(self):
        return self.messages.filter(is_read=False, recipient=self.request.user).count()


class Message(models.Model):
    chat: models.ForeignKey = models.ForeignKey(
        Chat,
        on_delete=models.CASCADE,
        related_name='messages',
        verbose_name='Chat'
    )
    sender: models.ForeignKey = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='sent_messages',
        verbose_name='Sender'
    )
    content: models.TextField = models.TextField(
        verbose_name='Message Content'
    )
    timestamp: models.DateTimeField = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Timestamp'
    )
    is_read: models.BooleanField = models.BooleanField(
        default=False,
        verbose_name='Is Read'
    )

    class Meta:
        verbose_name: str = 'Message'
        verbose_name_plural: str = 'Messages'
        ordering: List[str] = ['timestamp']

    def __str__(self) -> str:
        return f"Message from {self.sender.username} in chat {self.chat.id}"