from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Card

@login_required
def my_cards(request):
    user_cards = Card.objects.filter(user=request.user).order_by('-created_at')
    return render(request, 'cardspage/my_cards.html', {
        'user_cards': user_cards
    })