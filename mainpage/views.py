import logging

from django.conf import settings
from django.contrib import messages
from django.contrib.auth import login, authenticate, logout
from django.http import JsonResponse
from django.shortcuts import render, redirect
from .forms import CustomUserCreationForm, CustomAuthenticationForm
from .utils import send_verification_code

logger = logging.getLogger(__name__)


# Create your views here.
def home(request):
    return render(request,'mainpage/home_page.html')

def signup_view(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            try:
                user = form.save()
                user.backend = 'django.contrib.auth.backends.ModelBackend'
                login(request, user)
                messages.success(request, 'Registration successful!')
                return redirect('home')
            except Exception as e:
                logger.error(f'Error during registration: {e}')
                messages.error(request, 'Registration failed. Please try again.')
        else:
            logger.error(f'Form errors: {form.errors}')
            messages.error(request, 'Registration failed. Please check the form.')
    else:
        form = CustomUserCreationForm()

    return render(request, 'mainpage/signup_page.html', {'form': form})

def send_code_view(request):
    if request.method == 'POST':
        email = request.POST.get('email')

        # Отправляем код
        success, message = send_verification_code(email)

        if success:
            return JsonResponse({'status': 'success', 'message': message})
        else:
            return JsonResponse({'status': 'error', 'message': message}, status=400)
    return JsonResponse({'status': 'error', 'message': 'Недопустимый метод запроса.'}, status=405)

def login_view(request):
    """
    Функция для обработки входа пользователя.
    """
    if request.method == 'POST':
        form = CustomAuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)

                # Обработка чекбокса "Remember me"
                remember_me = request.POST.get('remember_me')
                if remember_me:
                    # Устанавливаем куки на 2 недели (14 дней)
                    request.session.set_expiry(settings.REMEMBER_ME_AGE)
                else:
                    # Куки истекают при закрытии браузера
                    request.session.set_expiry(0)

                messages.success(request, 'You have been logged in successfully!')
                return redirect('home')
            else:
                messages.error(request, 'Invalid username/email or password.')
        else:
            messages.error(request, 'Invalid username/email or password.')
    else:
        form = CustomAuthenticationForm()

    return render(request, 'mainpage/login_page.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('login')