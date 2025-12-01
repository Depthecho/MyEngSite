from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.views.decorators.http import require_http_methods, require_POST
from profilepage.forms import ProfileUpdateForm, UserUpdateForm, CustomPasswordChangeForm
from profilepage.models import Profile
from django.contrib.auth import update_session_auth_hash
from django.conf import settings
from django.utils.translation import get_language

def get_language_context():
    return {
        'LANGUAGES': settings.LANGUAGES,
        'current_language': get_language(),
    }

def settings_page(request):
    context = {
        'active_tab': 'main',
        'profile': request.user.profile
    }
    context.update(get_language_context())
    return render(request, 'settingspage/settings.html', context)

def language_settings(request):
    context = get_language_context()
    return render(request, 'settingspage/language_settings.html', context)


@login_required
@require_http_methods(["GET", "POST"])
def profile_settings(request):
    user = request.user
    profile = user.profile

    user_form = UserUpdateForm(instance=user)
    profile_form = ProfileUpdateForm(instance=profile)
    password_form = CustomPasswordChangeForm(user)

    if request.method == 'POST':
        if 'update_profile' in request.POST:
            user_form = UserUpdateForm(request.POST, instance=user)
            profile_form = ProfileUpdateForm(
                request.POST,
                request.FILES,
                instance=profile
            )

            if user_form.is_valid() and profile_form.is_valid():
                user_form.save()
                profile_form.save()
                messages.success(request, "Your profile has been updated successfully!")
                return redirect('profile_settings')
            else:
                messages.error(request, "Please correct the errors below.")

        elif 'change_password' in request.POST:
            password_form = CustomPasswordChangeForm(user, request.POST)
            if password_form.is_valid():
                user = password_form.save()
                update_session_auth_hash(request, user)
                messages.success(request, "Your password has been changed successfully!")
                return redirect('profile_settings')
            else:
                messages.error(request, "Please correct the password errors.")

    context = {
        'user_form': user_form,
        'profile_form': profile_form,
        'password_form': password_form,
        'profile': profile,
        'active_tab': 'profile',
    }
    context.update(get_language_context())

    return render(request, 'settingspage/profile_settings.html', context)

def privacy_and_security_settings(request):
    context = get_language_context()
    return render(request, 'settingspage/privacy_and_security.html', context)

def notifications_settings(request):
    context = get_language_context()
    return render(request, 'settingspage/notifications.html', context)

def appearance_settings(request):
    context = get_language_context()
    return render(request, 'settingspage/appearance.html', context)

def data_and_storage_settings(request):
    context = get_language_context()
    return render(request, 'settingspage/data_and_storage.html', context)

def help_and_support_settings(request):
    context = get_language_context()
    return render(request, 'settingspage/help_and_support.html', context)

def about_settings(request):
    context = get_language_context()
    return render(request, 'settingspage/about.html', context)

def privacy_policy(request):
    context = get_language_context()
    return render(request, 'settingspage/privacy_policy.html', context)

def terms_of_service(request):
    context = get_language_context()
    return render(request, 'settingspage/terms_of_service.html', context)

@login_required
@require_POST
def toggle_dark_mode(request):
    dark_mode = request.POST.get('dark_mode') == 'true'
    request.session['dark_mode'] = dark_mode
    return JsonResponse({'status': 'success'})