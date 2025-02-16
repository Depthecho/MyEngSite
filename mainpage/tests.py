from django.contrib.messages import get_messages
from django.test import TestCase, Client
from django.urls import reverse
from .models import CustomUser
from .forms import CustomUserCreationForm


class CustomUserModelText(TestCase):
    def setUp(self):
        """Подготовка данных для тестов модели."""
        self.user_data = {
            'username': 'testuser',
            'email': 'test@example.com',
            'password': 'testpass123',
        }
        self.superuser_data = {
            'username': 'admin',
            'email': 'admin@example.com',
            'password': 'adminpass123',
        }

    def test_create_user(self):
        """Тест создания обычного пользователя."""
        user = CustomUser.objects.create_user(**self.user_data)
        self.assertEqual(user.username, self.user_data['username'])
        self.assertEqual(user.email, self.user_data['email'])
        self.assertTrue(user.is_active)
        self.assertFalse(user.is_staff)
        self.assertFalse(user.is_superuser)

    def test_create_superuser(self):
        """Тест создания суперпользователя."""
        superuser = CustomUser.objects.create_superuser(**self.superuser_data)
        self.assertEqual(superuser.username, self.superuser_data['username'])
        self.assertEqual(superuser.email, self.superuser_data['email'])
        self.assertTrue(superuser.is_active)
        self.assertTrue(superuser.is_staff)
        self.assertTrue(superuser.is_superuser)

    def test_unique_username_and_email(self):
        """Тест уникальности username и email."""
        CustomUser.objects.create_user(
            username='testuser',
            email='test@example.com',
            password='testpass123'
        )
        # Попытка создать пользователя с таким же username
        with self.assertRaises(Exception):
            CustomUser.objects.create_user(
                username='testuser',
                email='test2@example.com',
                password='testpass123'
            )
        # Попытка создать пользователя с таким же email
        with self.assertRaises(Exception):
            CustomUser.objects.create_user(
                username='testuser2',
                email='test@example.com',
                password='testpass123'
            )


class CustomCreationFormTest(TestCase):
    def setUp(self):
        """Подготовка данных для тестов формы."""
        self.valid_data = {
            'username': 'testuser',
            'email': 'test@example.com',
            'password1': 'Testpass123',
            'password2': 'Testpass123',
        }
        self.existing_user = CustomUser.objects.create_user(
            username='existinguser',
            email='existing@example.com',
            password='testpass123'
        )

    def test_form_valid_data(self):
        """Тест формы с валидными данными."""
        form = CustomUserCreationForm(data=self.valid_data)
        self.assertTrue(form.is_valid())

    def test_form_invalid_email(self):
        """Тест формы с уже существующим email."""
        self.valid_data['email'] = self.existing_user.email
        form = CustomUserCreationForm(data=self.valid_data)
        self.assertFalse(form.is_valid())
        self.assertIn('email', form.errors)

    def test_form_invalid_username(self):
        """Тест формы с уже существующим username."""
        self.valid_data['username'] = self.existing_user.username
        form = CustomUserCreationForm(data=self.valid_data)
        self.assertFalse(form.is_valid())
        self.assertIn('username', form.errors)

    def test_form_password_too_short(self):
        """Тест формы с паролем менее 8 символов."""
        self.valid_data['password1'] = 'short'
        self.valid_data['password2'] = 'short'
        form = CustomUserCreationForm(data=self.valid_data)
        self.assertFalse(form.is_valid())
        self.assertIn('password1', form.errors)

    def test_form_password_no_letter_or_digit(self):
        """Тест формы с паролем без букв или цифр."""
        self.valid_data['password1'] = '12345678'
        self.valid_data['password2'] = '12345678'
        form = CustomUserCreationForm(data=self.valid_data)
        self.assertFalse(form.is_valid())
        self.assertIn('password1', form.errors)

    def test_form_passwords_do_not_match(self):
        """Тест формы с несовпадающими паролями."""
        self.valid_data['password2'] = 'Differentpass123'
        form = CustomUserCreationForm(data=self.valid_data)
        self.assertFalse(form.is_valid())
        self.assertIn('password2', form.errors)

class SignupViewsTest(TestCase):
    def setUp(self):
        """Подготовка данных для тестов представления."""
        self.client = Client()
        self.signup_url = reverse('signup')
        self.valid_data = {
            'username': 'testuser',
            'email': 'test@example.com',
            'password1': 'Testpass123',
            'password2': 'Testpass123',
        }

    def test_signup_view_get(self):
        """Тест отображения формы регистрации."""
        response = self.client.get(self.signup_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'mainpage/signup_page.html')
        self.assertIsInstance(response.context['form'], CustomUserCreationForm)


    def test_signup_view_post_valid_data(self):
        """Тест успешной регистрации с валидными данными."""
        response = self.client.post(self.signup_url, data=self.valid_data)
        self.assertEqual(response.status_code, 302)  # Проверка перенаправления после успешной регистрации
        self.assertTrue(CustomUser.objects.filter(username='testuser').exists())

    def test_signup_view_post_invalid_data(self):
        """Тест регистрации с невалидными данными."""
        self.valid_data['email'] = 'invalid-email'
        response = self.client.post(self.signup_url, data=self.valid_data)
        self.assertEqual(response.status_code, 200)  # Форма не прошла валидацию, страница отображается снова
        self.assertFalse(CustomUser.objects.filter(username='testuser').exists())


class LoginViewTest(TestCase):
    def setUp(self):
        """Подготовка данных для тестов."""
        self.client = Client()
        self.login_url = reverse('login')
        self.home_url = reverse('home')
        self.user = CustomUser.objects.create_user(
            username='testuser',
            email='test@example.com',
            password='testpass123'
        )

    def test_login_with_username(self):
        """Тест успешного входа по username."""
        response = self.client.post(self.login_url, {
            'username': 'testuser',
            'password': 'testpass123',
        })
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, self.home_url)

    def test_login_with_email(self):
        """Тест успешного входа по email."""
        response = self.client.post(self.login_url, {
            'username': 'test@example.com',
            'password': 'testpass123',
        })
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, self.home_url)

    def test_login_with_invalid_username(self):
        """Тест входа с неверным username."""
        response = self.client.post(self.login_url, {
            'username': 'wronguser',
            'password': 'testpass123',
        })
        self.assertEqual(response.status_code, 200)
        messages = list(get_messages(response.wsgi_request))
        self.assertEqual(len(messages), 1)
        self.assertEqual(str(messages[0]), 'Invalid username/email or password.')

    def test_login_with_invalid_password(self):
        """Тест входа с неверным паролем."""
        response = self.client.post(self.login_url, {
            'username': 'testuser',
            'password': 'wrongpassword',
        })
        self.assertEqual(response.status_code, 200)
        messages = list(get_messages(response.wsgi_request))
        self.assertEqual(len(messages), 1)
        self.assertEqual(str(messages[0]), 'Invalid username/email or password.')