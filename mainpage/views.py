from django.conf import settings
from django.utils import timezone
from celery.beat import logger
from django.contrib.auth import logout
from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse, JsonResponse
from django.contrib.auth.models import AbstractBaseUser
from typing import Any, Dict, Tuple, Optional
from .forms import CustomUserCreationForm, CustomAuthenticationForm
from .services import UserRegistrationService, UserAuthenticationService, ProfileStreakService # <--- Добавлен импорт
from .decorators import handle_errors
from .utils import send_verification_code
from profilepage.models import Profile


@handle_errors
def home(request: HttpRequest) -> HttpResponse:
    context = {
        'LANGUAGES': settings.LANGUAGES,
    }
    if request.user.is_authenticated:
        try:
            profile = request.user.profile
            context['profile'] = profile

            # Делегируем логику обновления стрика новому сервису
            ProfileStreakService.update_streak(profile)

        except Profile.DoesNotExist:
            # Если профиль не существует, это указывает на проблему,
            # так как профиль должен создаваться вместе с пользователем.
            # Возможно, стоит пересмотреть процесс создания пользователя/профиля.
            # Для предотвращения ошибок, можно здесь создать профиль,
            # но это может скрыть более глубокие проблемы.
            logger.error(f"Profile does not exist for user {request.user.id}")
            pass # Или handle error, create profile, redirect etc.
    return render(request, 'mainpage/home_page.html', context)


@handle_errors
def signup_view(request: HttpRequest) -> HttpResponse:
    if request.method == 'POST':
        form: CustomUserCreationForm = CustomUserCreationForm(request.POST)
        user: AbstractBaseUser = UserRegistrationService.register_user(form, request)
        return redirect('home')
    else:
        form: CustomUserCreationForm = CustomUserCreationForm()
    return render(request, 'mainpage/signup_page.html', {'form': form, 'LANGUAGES': settings.LANGUAGES,})


@handle_errors
def send_code_view(request: HttpRequest) -> JsonResponse:
    logger.info(f"Request to send code: {request.POST}")
    if request.method == 'POST':
        email: Optional[str] = request.POST.get('email')
        if not email:
            logger.warning("No email provided")
            return JsonResponse(
                {'status': 'error', 'message': 'Email обязателен.'},
                status=400
            )

        logger.info(f"Processing email: {email}")
        success: bool
        message: str
        success, message = send_verification_code(email)
        logger.info(f"Send result: {success}, {message}")

        if success:
            return JsonResponse({'status': 'success', 'message': message})
        else:
            return JsonResponse(
                {'status': 'error', 'message': message},
                status=400
            )
    return JsonResponse(
        {'status': 'error', 'message': 'Недопустимый метод запроса.'},
        status=405
    )


@handle_errors
def login_view(request: HttpRequest) -> HttpResponse:
    if request.method == 'POST':
        form: CustomAuthenticationForm = CustomAuthenticationForm(request, data=request.POST)
        user: Optional[AbstractBaseUser] = UserAuthenticationService.authenticate_user(request, form)
        if user:
            return redirect('home')
    else:
        form: CustomAuthenticationForm = CustomAuthenticationForm()
    return render(request, 'mainpage/login_page.html', {'form': form, 'LANGUAGES': settings.LANGUAGES,})


@handle_errors
def logout_view(request: HttpRequest) -> HttpResponse:
    logout(request)
    return redirect('login')