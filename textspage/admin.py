from django.contrib import admin
from .models import Text

@admin.register(Text)
class TextAdmin(admin.ModelAdmin):
    list_display = ('title', 'content', 'length', 'english_level', 'created_at', 'added_by')
    search_fields = ('title',)