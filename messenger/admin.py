from django.contrib import admin
from .models import Chat, Message


@admin.register(Chat)
class ChatAdmin(admin.ModelAdmin):
    list_display = ('id', 'display_participants', 'created_at', 'updated_at', 'last_message_preview')
    list_filter = ('created_at', 'updated_at')
    search_fields = ('id', 'participants__username')
    readonly_fields = ('id', 'created_at', 'updated_at')
    filter_horizontal = ('participants',)

    def display_participants(self, obj):
        return ", ".join([user.username for user in obj.participants.all()])

    display_participants.short_description = 'Participants'

    def last_message_preview(self, obj):
        last_msg = obj.get_last_message
        return last_msg.content[:50] + '...' if last_msg else 'No messages'

    last_message_preview.short_description = 'Last Message'


@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = ('id', 'short_content', 'sender', 'chat_id', 'timestamp', 'is_read')
    list_filter = ('is_read', 'timestamp', 'sender')
    search_fields = ('content', 'sender__username', 'chat__id')
    readonly_fields = ('timestamp',)
    date_hierarchy = 'timestamp'

    def short_content(self, obj):
        return obj.content[:50] + '...' if len(obj.content) > 50 else obj.content

    short_content.short_description = 'Content'

    def chat_id(self, obj):
        return obj.chat.id

    chat_id.short_description = 'Chat ID'