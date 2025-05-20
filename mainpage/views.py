from django.contrib.auth import logout
from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse, JsonResponse
from django.contrib.auth.models import AbstractBaseUser
from typing import Any, Dict, Tuple, Optional
from .forms import CustomUserCreationForm, CustomAuthenticationForm
from .services import UserRegistrationService, UserAuthenticationService
from .decorators import handle_errors
from .utils import send_verification_code


@handle_errors
def home(request: HttpRequest) -> HttpResponse:
    return render(request, 'mainpage/home_page.html')


@handle_errors
def signup_view(request: HttpRequest) -> HttpResponse:
    if request.method == 'POST':
        form: CustomUserCreationForm = CustomUserCreationForm(request.POST)
        user: AbstractBaseUser = UserRegistrationService.register_user(form, request)
        return redirect('home')
    else:
        form: CustomUserCreationForm = CustomUserCreationForm()
    return render(request, 'mainpage/signup_page.html', {'form': form})


@handle_errors
def send_code_view(request: HttpRequest) -> JsonResponse:
    if request.method == 'POST':
        email: Optional[str] = request.POST.get('email')
        if not email:
            return JsonResponse(
                {'status': 'error', 'message': 'Email обязателен.'},
                status=400
            )

        success: bool
        message: str
        success, message = send_verification_code(email)

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
    return render(request, 'mainpage/login_page.html', {'form': form})


@handle_errors
def logout_view(request: HttpRequest) -> HttpResponse:
    logout(request)
    return redirect('login')