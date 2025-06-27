from django.db.models import QuerySet, Q, Count, Max, F
from django.contrib.auth.models import AbstractUser
from .models import Chat, Message
from mainpage.models import CustomUser
from typing import Optional, Set, List


class ChatService:
    @staticmethod
    def get_user_chats(user: AbstractUser) -> QuerySet[Chat]:
        return Chat.objects.filter(participants=user).annotate(
            last_message_date=Max('messages__timestamp'),
            unread_count_annotated=Count(
                'messages',
                filter=Q(messages__is_read=False) & ~Q(messages__sender=user)
            )
        ).order_by(F('last_message_date').desc(nulls_last=True))

    @staticmethod
    def get_friends_without_chat(user: AbstractUser, friends: QuerySet[CustomUser]) -> List[CustomUser]:
        chats: QuerySet[Chat] = ChatService.get_user_chats(user)
        friends_with_chats_ids: Set[int] = set()

        for chat in chats:
            for participant in chat.participants.all():
                if participant != user:
                    friends_with_chats_ids.add(participant.id)

        return [friend for friend in friends if friend.id not in friends_with_chats_ids]

    @staticmethod
    def get_or_create_chat(user1: AbstractUser, user2: AbstractUser) -> Optional[Chat]:
        if user1 == user2:
            return None

        existing_chat: Optional[Chat] = Chat.objects.filter(
            participants=user1
        ).filter(
            participants=user2
        ).annotate(num_participants=Count('participants')).filter(num_participants=2).first()

        if existing_chat:
            return existing_chat

        new_chat: Chat = Chat.objects.create()
        new_chat.participants.add(user1, user2)
        return new_chat

    @staticmethod
    def search_user_chats(user: AbstractUser, query: str) -> QuerySet[Chat]:
        return Chat.objects.filter(
            participants=user
        ).filter(
            Q(participants__username__icontains=query)
        ).annotate(
            last_message_date=Max('messages__timestamp'),
            unread_count_annotated=Count(
                'messages',
                filter=Q(messages__is_read=False) & ~Q(messages__sender=user)
            )
        ).distinct().order_by(F('last_message_date').desc(nulls_last=True))


class MessageService:
    @staticmethod
    def mark_messages_as_read(chat: Chat, user: AbstractUser) -> None:
        chat.messages.filter(is_read=False).exclude(sender=user).update(is_read=True)

    @staticmethod
    def create_message(chat: Chat, sender: AbstractUser, form_data) -> Message:
        message: Message = form_data.save(commit=False)
        message.chat = chat
        message.sender = sender
        message.is_read = False
        message.save()
        return message