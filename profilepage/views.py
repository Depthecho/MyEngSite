from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from .models import Profile


@login_required
def profile_page(request):
    try:
        user_profile = Profile.objects.get(user=request.user)
    except Profile.DoesNotExist:
        user_profile = Profile.objects.create(
            user=request.user,
            username=request.user.username,
            email=request.user.email,
            first_name='',
            last_name=''
        )

    return render(request, 'profilepage/profile_page.html', {'profile': user_profile})