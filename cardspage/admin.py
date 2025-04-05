from django.contrib import admin
from .models import Card  # Импортируем модель Card

@admin.register(Card)
class CardAdmin(admin.ModelAdmin):
    list_display = ('english_word', 'native_translation', 'user', 'category', 'created_at')
    list_filter = ('user', 'category', 'created_at')
    search_fields = ('english_word', 'native_translation')
    ordering = ('-created_at',)