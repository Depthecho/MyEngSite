from django.contrib.auth.decorators import login_required
from django.shortcuts import render, HttpResponseRedirect
from django.http import HttpRequest, HttpResponse
from django.forms import Form
from typing import Any, Dict
from .services import ProfileService, ProfileUpdateHandler
from .models import Profile


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