from django.contrib import admin
from .models import Profile

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = (
        'user__username',
        'user__email',
        'user__first_name',
        'user__last_name',
        'words_learned',
        'texts_read',
        'tests_completed',
        'streak',
    )
    search_fields = (
        'user__username',
        'user__email',
        'user__first_name',
        'user__last_name',
    )

    list_filter = ('english_level', 'study_start_date')
    raw_id_fields = ('user',)