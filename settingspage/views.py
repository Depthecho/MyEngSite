from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.views.decorators.http import require_http_methods
from profilepage.forms import ProfileUpdateForm, UserUpdateForm, CustomPasswordChangeForm
from profilepage.models import Profile
from django.contrib.auth import update_session_auth_hash

def settings_page(request):
    return render(request, 'settingspage/settings.html', {
        'active_tab': 'main',
        'profile': request.user.profile
    })

def language_settings(request):
    return render(request, 'settingspage/language_settings.html')


@login_required
@require_http_methods(["GET", "POST"])
def profile_settings(request):
    user = request.user
    profile = user.profile

    # Инициализация форм
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

    return render(request, 'settingspage/profile_settings.html', context)