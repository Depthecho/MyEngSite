from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Card
from .forms import CardForm
from .services import CardService


@login_required
def my_cards(request):
    user_cards = CardService.get_user_cards(request.user)
    return render(request, 'cardspage/my_cards.html', {'user_cards': user_cards})


@login_required
def add_cards(request):
    if request.method == 'POST':
        form = CardForm(request.POST)
        if form.is_valid():
            CardService.create_card(form, request.user)
            return redirect('add_cards' if 'add_another' in request.POST else 'my_cards')
    else:
        form = CardForm()

    recent_cards = CardService.get_user_cards(request.user, 8)
    return render(request, 'cardspage/add_cards.html', {
        'form': form,
        'recent_cards': recent_cards
    })


@login_required
def edit_card(request, card_id):
    card = get_object_or_404(Card, id=card_id, user=request.user)

    if request.method == 'POST':
        form = CardForm(request.POST, instance=card)
        if form.is_valid():
            form.save()
            return redirect('my_cards')
    else:
        form = CardForm(instance=card)

    return render(request, 'cardspage/edit_card.html', {
        'form': form,
        'card': card
    })


@login_required
def delete_card(request, card_id):
    if request.method == 'POST':
        CardService.delete_card(card_id, request.user)
        return redirect('my_cards')

    # Для GET запроса показываем подтверждение удаления
    card = get_object_or_404(Card, id=card_id, user=request.user)
    return render(request, 'cardspage/confirm_card_delete.html', {'card': card})