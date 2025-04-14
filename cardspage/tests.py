import pytest
from io import BytesIO
from PIL import Image
from django.urls import reverse
from mainpage.models import CustomUser as User
from django.contrib.auth.hashers import check_password
from django.contrib.messages import get_messages
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import update_session_auth_hash
from profilepage.models import Profile, Achievement
from profilepage.services import ProfileService, ProfileUpdateHandler, AchievementChecker
from profilepage.forms import ProfileUpdateForm, CustomPasswordChangeForm
from unittest.mock import MagicMock, patch


# Фикстуры
@pytest.fixture
def test_user(db):
    return User.objects.create_user(
        username='testuser',
        email='test@example.com',
        password='password'
    )


@pytest.fixture
def test_profile(db, test_user):
    profile, _ = Profile.objects.get_or_create(
        user=test_user,
        defaults={
            'username': 'testuser',
            'email': 'test@example.com',
            'first_name': '',
            'last_name': ''
        }
    )
    return profile


@pytest.fixture
def test_image():
    file = BytesIO()
    image = Image.new('RGB', (100, 100))
    image.save(file, 'png')
    file.name = 'test.png'
    file.seek(0)
    return file


# Тесты
@pytest.mark.django_db
class TestProfileService:
    def test_get_or_create_profile(self, test_user):
        service = ProfileService(test_user)
        profile = service.get_or_create_profile()
        assert profile.user == test_user
        assert profile.username == 'testuser'

    def test_check_achievements(self, test_user):
        profile = Profile.objects.create(
            user=test_user,
            words_learned=600,
            texts_read=200,
            tests_completed=500
        )

        # Очищаем существующие достижения
        Achievement.objects.filter(user=test_user).delete()

        service = ProfileService(test_user)
        service.check_achievements()

        achievements = Achievement.objects.filter(user=test_user)
        assert achievements.count() == 3  # По одному достижению каждого типа


@pytest.mark.django_db
class TestProfileUpdateHandler:
    def test_get_forms(self, test_user):
        request = MagicMock(user=test_user)
        handler = ProfileUpdateHandler(request)

        forms = handler.get_forms()
        assert isinstance(forms['profile_form'], ProfileUpdateForm)
        assert isinstance(forms['password_form'], CustomPasswordChangeForm)

    def test_process_profile_update(self, test_user):
        profile = Profile.objects.create(user=test_user)
        request = MagicMock(
            user=test_user,
            POST={
                'update_profile': '1',
                'first_name': 'John',
                'last_name': 'Doe',
                'email': 'john@example.com'
            },
            FILES={},
            method='POST'
        )

        handler = ProfileUpdateHandler(request)
        response = handler.process_update()

        profile.refresh_from_db()
        assert profile.first_name == 'John'
        assert profile.last_name == 'Doe'
        assert response.status_code == 302

    def test_process_password_change(self, test_user):
        request = MagicMock(
            user=test_user,
            POST={
                'change_password': '1',
                'old_password': 'password',
                'new_password1': 'newpass123',
                'new_password2': 'newpass123'
            },
            FILES={},
            method='POST'
        )

        with patch('django.contrib.auth.update_session_auth_hash') as mock_update:
            handler = ProfileUpdateHandler(request)
            response = handler.process_update()

            mock_update.assert_called_once()
            test_user.refresh_from_db()
            assert test_user.check_password('newpass123')
            assert response.status_code == 302

    def test_avatar_upload(self, test_user, test_image):
        profile = Profile.objects.create(user=test_user)
        request = MagicMock(
            user=test_user,
            POST={'update_profile': '1'},
            FILES={'avatar': test_image},
            method='POST'
        )

        handler = ProfileUpdateHandler(request)
        handler.process_update()

        profile.refresh_from_db()
        assert profile.avatar


@pytest.mark.django_db
class TestAchievementChecker:
    def test_check_achievements(self, test_user):
        profile = Profile.objects.create(
            user=test_user,
            words_learned=600,
            texts_read=200,
            tests_completed=500
        )

        Achievement.objects.filter(user=test_user).delete()
        AchievementChecker.check_achievements(test_user, profile)

        achievements = Achievement.objects.filter(user=test_user)
        assert achievements.count() == 3

    def test_achievement_levels(self, test_user):
        # Создаем временный профиль
        Profile.objects.filter(user=test_user).delete()
        profile = Profile.objects.create(user=test_user)

        test_cases = [
            ('words', 100, 1),
            ('words', 500, 2),
            ('words', 1500, 3),
            ('texts', 50, 1),
            ('tests', 500, 3)
        ]

        for badge_type, value, expected_level in test_cases:
            # Очищаем предыдущие достижения
            Achievement.objects.filter(user=test_user, badge_type=badge_type).delete()

            setattr(profile,
                    f"{badge_type}_learned" if badge_type == 'words' else
                    f"{badge_type}_read" if badge_type == 'texts' else
                    f"{badge_type}_completed",
                    value)
            profile.save()

            AchievementChecker.check_achievements(test_user, profile)
            achievement = Achievement.objects.filter(
                user=test_user,
                badge_type=badge_type
            ).first()
            assert achievement.level == expected_level

    def test_threshold_boundaries(self, test_user):
        Profile.objects.filter(user=test_user).delete()
        profile = Profile.objects.create(user=test_user)

        for value, should_have_achievement in [(99, False), (100, True), (101, True)]:
            Achievement.objects.filter(user=test_user).delete()
            profile.words_learned = value
            profile.save()

            AchievementChecker.check_achievements(test_user, profile)
            assert Achievement.objects.filter(user=test_user).exists() == should_have_achievement


@pytest.mark.django_db
def test_profile_page_view(client, test_user):
    profile = Profile.objects.create(
        user=test_user,
        first_name='John',
        last_name='Doe'
    )

    client.force_login(test_user)
    response = client.get(reverse('profile'))

    assert response.status_code == 200
    content = response.content.decode()
    assert 'John' in content or 'value="John"' in content
    assert 'Doe' in content or 'value="Doe"' in content


@pytest.mark.django_db
def test_update_profile_post(client, test_user):
    profile = Profile.objects.create(user=test_user)
    client.force_login(test_user)

    response = client.post(reverse('update_profile'), {
        'update_profile': '1',
        'first_name': 'Jane',
        'last_name': 'Smith',
        'email': 'jane@example.com'
    }, follow=True)

    assert response.status_code == 200
    profile.refresh_from_db()
    assert profile.first_name == 'Jane'


@pytest.mark.django_db
def test_password_change_view(client, test_user):
    client.force_login(test_user)
    response = client.post(reverse('update_profile'), {
        'change_password': '1',
        'old_password': 'password',
        'new_password1': 'newpass123',
        'new_password2': 'newpass123'
    }, follow=True)

    assert response.status_code == 200
    test_user.refresh_from_db()
    assert test_user.check_password('newpass123')


@pytest.mark.django_db
def test_avatar_upload_view(client, test_user, test_image):
    Profile.objects.create(user=test_user)
    client.force_login(test_user)

    with open(test_image.name, 'wb') as f:
        f.write(test_image.getvalue())

    with open(test_image.name, 'rb') as img:
        response = client.post(reverse('update_profile'), {
            'update_profile': '1',
            'avatar': img
        }, format='multipart', follow=True)

    assert response.status_code == 200
    assert Profile.objects.get(user=test_user).avatar


@pytest.mark.django_db
class TestForms:
    def test_profile_update_form_valid(self):
        user = User.objects.create_user(username='testuser', email='test@example.com', password='password')
        profile = Profile.objects.create(user=user)

        form_data = {
            'username': 'testuser',
            'first_name': 'John',
            'last_name': 'Doe',
            'email': 'valid@example.com'
        }
        form = ProfileUpdateForm(data=form_data, instance=profile)
        assert form.is_valid()

    def test_profile_update_form_invalid_email(self):
        user = User.objects.create_user(username='testuser', email='test@example.com', password='password')
        profile = Profile.objects.create(user=user)

        form_data = {
            'username': 'testuser',
            'first_name': 'John',
            'last_name': 'Doe',
            'email': 'invalid-email'
        }
        form = ProfileUpdateForm(data=form_data, instance=profile)

        assert not form.is_valid()
        assert 'email' in form.errors

    def test_password_change_form_valid(self, test_user):
        form_data = {
            'old_password': 'password',
            'new_password1': 'newpass123',
            'new_password2': 'newpass123'
        }
        form = CustomPasswordChangeForm(test_user, data=form_data)
        assert form.is_valid()