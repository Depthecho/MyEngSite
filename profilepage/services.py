from django.utils import timezone
from .models import Profile, Achievement
from .forms import ProfileUpdateForm, CustomPasswordChangeForm
from django.contrib import messages
from django.shortcuts import redirect


class ProfileUpdateHandler:
    def __init__(self, request):
        self.request = request
        self.profile = request.user.profile

    def process_update(self):
        form = self._get_appropriate_form()

        if not form or not form.is_valid():
            return form

        self._save_form(form)
        self._add_success_message()
        return redirect('profile')

    def _get_appropriate_form(self):
        if 'update_profile' in self.request.POST:
            return ProfileUpdateForm(
                self.request.POST,
                self.request.FILES,
                instance=self.profile
            )
        elif 'change_password' in self.request.POST:
            return CustomPasswordChangeForm(
                self.request.user,
                self.request.POST
            )
        return None

    def _save_form(self, form):
        if isinstance(form, CustomPasswordChangeForm):
            user = form.save()
            update_session_auth_hash(self.request, user)
        else:
            form.save()

    def _add_success_message(self):
        message = (
            "Password updated successfully!"
            if 'change_password' in self.request.POST
            else "Your profile has been updated!"
        )
        messages.success(self.request, message)

    def get_forms(self):
        return {
            'profile_form': ProfileUpdateForm(instance=self.profile),
            'password_form': CustomPasswordChangeForm(self.request.user)
        }


class AchievementChecker:

    ACHIEVEMENT_THRESHOLDS = {
        'words': {1: 100, 2: 500, 3: 1500},
        'texts': {1: 50, 2: 150, 3: 500},
        'tests': {1: 50, 2: 150, 3: 500}
    }

    @classmethod
    def check_achievements(cls, user, profile):
        for badge_type in cls.ACHIEVEMENT_THRESHOLDS:
            cls._check_single_type(user, profile, badge_type)

    @classmethod
    def _check_single_type(cls, user, profile, badge_type):
        current_value = getattr(profile,
                                f"{badge_type}_learned" if badge_type == 'words' else f"{badge_type}_read" if badge_type == 'texts' else f"{badge_type}_completed")

        for level, threshold in cls.ACHIEVEMENT_THRESHOLDS[badge_type].items():
            if current_value >= threshold:
                Achievement.objects.get_or_create(
                    user=user,
                    badge_type=badge_type,
                    level=level,
                    defaults={'achieved_at': timezone.now()}
                )


class ProfileService:

    def __init__(self, user):
        self.user = user

    def get_or_create_profile(self):
        profile, _ = Profile.objects.get_or_create(
            user=self.user,
            defaults={
                'username': self.user.username,
                'email': self.user.email,
                'first_name': '',
                'last_name': ''
            }
        )
        return profile

    def check_achievements(self):
        profile = self.get_or_create_profile()
        AchievementChecker.check_achievements(self.user, profile)
        return True