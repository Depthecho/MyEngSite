from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404
from .models import Profile
from .services import ProfileService


@login_required
def profile_page(request):
    """View для отображения профиля пользователя с достижениями."""
    profile_service = ProfileService(request.user)
    user_profile = profile_service.get_or_create_profile()
    profile_service.check_achievements()

    return render(request, 'profilepage/profile_page.html', {
        'profile': user_profile,
        'achievements': user_profile.get_achievements()
    })