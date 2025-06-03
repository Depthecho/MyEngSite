from django.contrib.auth.decorators import login_required
from django.core.exceptions import PermissionDenied
from django.shortcuts import render, HttpResponseRedirect, get_object_or_404
from django.http import HttpRequest, HttpResponse
from django.forms import Form
from typing import Any, Dict
from django.urls import reverse
from .services import ProfileService, ProfileUpdateHandler
from .models import Profile, UserModel


@login_required
def profile_page(request: HttpRequest) -> HttpResponse:
    profile_service: ProfileService = ProfileService(request.user)
    user_profile: Profile = profile_service.get_or_create_profile()
    profile_service.check_achievements()

    return render(request, 'profilepage/profile_page.html', {
        'profile': user_profile,
        'achievements': user_profile.get_achievements()
    })


@login_required
def update_profile(request: HttpRequest) -> HttpResponse:
    handler: ProfileUpdateHandler = ProfileUpdateHandler(request)

    if request.method == 'POST':
        result: Union[Form, HttpResponseRedirect] = handler.process_update()
        if result and not hasattr(result, 'is_valid'):
            return result

    context: Dict[str, Any] = handler.get_forms()
    context['profile'] = request.user.profile

    return render(request, 'profilepage/update_profile.html', context)


@login_required
def public_profile(request: HttpRequest, username: str) -> HttpResponse:
    # Получаем профиль по username
    user_profile = get_object_or_404(Profile, username=username)

    # Проверяем, что это не профиль текущего пользователя
    if user_profile.user == request.user:
        return HttpResponseRedirect(reverse('profile'))

    # Проверяем настройки приватности
    if not _check_profile_visibility(user_profile, request.user):
        raise PermissionDenied("You don't have permission to view this profile")

    return render(request, 'profilepage/public_profile.html', {
        'profile': user_profile,
        'achievements': user_profile.get_achievements(),
        'is_owner': False
    })


def _check_profile_visibility(profile: Profile, viewer: UserModel) -> bool:
    return True