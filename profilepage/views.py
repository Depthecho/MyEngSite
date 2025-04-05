from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from .services import ProfileService, ProfileUpdateHandler


@login_required
def profile_page(request):
    profile_service = ProfileService(request.user)
    user_profile = profile_service.get_or_create_profile()
    profile_service.check_achievements()

    return render(request, 'profilepage/profile_page.html', {
        'profile': user_profile,
        'achievements': user_profile.get_achievements()
    })


@login_required
def update_profile(request):
    """Тонкий view-слой, только маршрутизация"""
    handler = ProfileUpdateHandler(request)

    if request.method == 'POST':
        result = handler.process_update()
        if result and not hasattr(result, 'is_valid'):  # Если это redirect
            return result

    context = handler.get_forms()
    context['profile'] = request.user.profile

    return render(request, 'profilepage/update_profile.html', context)