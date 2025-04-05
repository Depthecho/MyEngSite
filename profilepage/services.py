from .models import Profile


class ProfileService:
    def __init__(self, user):
        self.user = user

    def get_or_create_profile(self):
        profile, created = Profile.objects.get_or_create(
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
        self._check_words_achievements(profile)
        self._check_texts_achievements(profile)
        self._check_tests_achievements(profile)
        return True

    def _check_words_achievements(self, profile):
        thresholds = {1: 100, 2: 500, 3: 1500}
        self._check_achievement_type(profile, 'words', profile.words_learned, thresholds)

    def _check_texts_achievements(self, profile):
        thresholds = {1: 50, 2: 150, 3: 500}
        self._check_achievement_type(profile, 'texts', profile.texts_read, thresholds)

    def _check_tests_achievements(self, profile):
        thresholds = {1: 50, 2: 150, 3: 500}
        self._check_achievement_type(profile, 'tests', profile.tests_completed, thresholds)

    def _check_achievement_type(self, profile, badge_type, current_value, thresholds):
        from django.utils import timezone
        from .models import Achievement

        for level, threshold in thresholds.items():
            if current_value >= threshold:
                Achievement.objects.get_or_create(
                    user=self.user,
                    badge_type=badge_type,
                    level=level,
                    defaults={'achieved_at': timezone.now()}
                )