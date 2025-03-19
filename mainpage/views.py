from django.contrib.auth import logout
from django.shortcuts import render, redirect
from django.http import JsonResponse
from .forms import CustomUserCreationForm, CustomAuthenticationForm
from .services import UserRegistrationService, UserAuthenticationService
from .decorators import handle_errors
from .utils import send_verification_code

@handle_errors
def home(request):
    return render(request, 'mainpage/home_page.html')

@handle_errors
def signup_view(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        UserRegistrationService.register_user(form, request)
        return redirect('home')
    else:
        form = CustomUserCreationForm()
    return render(request, 'mainpage/signup_page.html', {'form': form})

@handle_errors
def send_code_view(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        success, message = send_verification_code(email)
        if success:
            return JsonResponse({'status': 'success', 'message': message})
        else:
            return JsonResponse({'status': 'error', 'message': message}, status=400)
    return JsonResponse({'status': 'error', 'message': 'Недопустимый метод запроса.'}, status=405)

@handle_errors
def login_view(request):
    if request.method == 'POST':
        form = CustomAuthenticationForm(request, data=request.POST)
        user = UserAuthenticationService.authenticate_user(request, form)
        if user:
            return redirect('home')
    else:
        form = CustomAuthenticationForm()
    return render(request, 'mainpage/login_page.html', {'form': form})

@handle_errors
def logout_view(request):
    logout(request)
    return redirect('login')