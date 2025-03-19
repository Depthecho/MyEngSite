from django.contrib import admin
from .models import Profile

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'first_name', 'last_name', 'words_learned', 'texts_read', 'tests_completed', 'streak')
    search_fields = ('username', 'email')