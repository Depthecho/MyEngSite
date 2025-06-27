from django.contrib import messages
from django.contrib.auth import get_user_model
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.http import HttpRequest, HttpResponse
from django.db.models import QuerySet
from .models import Chat
from .forms import MessageForm
from mainpage.models import CustomUser
from .services import ChatService, MessageService
from typing import Optional, Set

User = get_user_model()


@login_required
def chat_list(request: HttpRequest) -> HttpResponse:
    search_query = request.GET.get('q', '')
    chats = ChatService.get_user_chats(request.user)

    search_results = None
    if search_query:
        search_results = ChatService.search_user_chats(request.user, search_query)

    all_friends = request.user.profile.get_friends()
    friends_without_chat = ChatService.get_friends_without_chat(request.user, all_friends)

    context = {
        'chats': chats,
        'friends_without_chat': friends_without_chat,
        'current_chat_id': None,
        'search_query': search_query,
        'search_results': search_results,
    }
    return render(request, 'messenger/chat_list.html', context)


@login_required
def chat_detail(request: HttpRequest, chat_id: int) -> HttpResponse:
    chat: Chat = get_object_or_404(Chat, id=chat_id, participants=request.user)
    messages_in_chat: QuerySet[Message] = chat.messages.all().order_by('timestamp')
    MessageService.mark_messages_as_read(chat, request.user)
    all_user_chats: QuerySet[Chat] = ChatService.get_user_chats(request.user)

    if request.method == 'POST':
        form: MessageForm = MessageForm(request.POST)
        if form.is_valid():
            MessageService.create_message(chat, request.user, form)
            return redirect('chat_detail', chat_id=chat.id)
    else:
        form: MessageForm = MessageForm()

    context: dict = {
        'chat': chat,
        'messages': messages_in_chat,
        'form': form,
        'chats': all_user_chats,
        'current_chat_id': chat_id,
    }
    return render(request, 'messenger/chat_detail.html', context)


@login_required
def start_chat(request: HttpRequest, user_id: int) -> HttpResponse:
    other_user: CustomUser = get_object_or_404(CustomUser, id=user_id)
    chat: Optional[Chat] = ChatService.get_or_create_chat(request.user, other_user)

    if not chat:
        messages.warning(request, "Вы не можете начать чат с самим собой.")
        return redirect('chat_list')

    messages.success(request, f"Чат с {other_user.username} успешно создан.")
    return redirect('messenger:chat_detail', chat_id=chat.id)


@login_required
def select_friend_for_chat(request: HttpRequest) -> HttpResponse:
    friends: QuerySet[CustomUser] = request.user.profile.get_friends()
    chats: QuerySet[Chat] = ChatService.get_user_chats(request.user)
    friends_with_existing_chats_ids: Set[int] = set()

    for chat in chats:
        for participant in chat.participants.all():
            if participant != request.user:
                friends_with_existing_chats_ids.add(participant.id)

    friends_to_chat_with: List[CustomUser] = [
        friend for friend in friends
        if friend.id not in friends_with_existing_chats_ids
    ]

    context: dict = {
        'friends_to_chat_with': friends_to_chat_with,
        'chats': chats,
        'current_chat_id': None,
    }
    return render(request, 'messenger/select_friend_for_chat.html', context)


@login_required
def send_message(request: HttpRequest, chat_id: int) -> HttpResponse:
    chat: Chat = get_object_or_404(Chat, id=chat_id)

    if request.user not in chat.participants.all():
        return redirect('messenger:chat_list')

    if request.method == 'POST':
        form: MessageForm = MessageForm(request.POST)
        if form.is_valid():
            MessageService.create_message(chat, request.user, form)
            return redirect('messenger:chat_detail', chat_id=chat.id)

    return redirect('messenger:chat_detail', chat_id=chat.id)