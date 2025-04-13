from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Card
from .forms import CardForm
from .services import CardQueryService, CardCRUDService, QuizService


@login_required
def my_cards(request):
    context = CardQueryService.build_my_cards_context(request.user, request.GET)
    return render(request, 'cardspage/my_cards.html', context)


@login_required
def add_cards(request):
    if request.method == 'POST':
        form = CardForm(request.POST)
        if form.is_valid():
            CardCRUDService.create_card(form, request.user)
            return redirect('add_cards' if 'add_another' in request.POST else 'my_cards')

    form = form if request.method == 'POST' else CardForm()
    return render(request, 'cardspage/add_cards.html', {
        'form': form,
        'recent_cards': CardQueryService.get_recent_cards(request.user)
    })


@login_required
def edit_card(request, user_card_id):
    card = get_object_or_404(Card, user=request.user, user_card_id=user_card_id)

    if request.method == 'POST':
        form = CardForm(request.POST, instance=card)
        if form.is_valid():
            CardCRUDService.update_card(form)
            return redirect('my_cards')

    form = CardForm(instance=card)
    return render(request, 'cardspage/edit_card.html', {'form': form, 'card': card})


@login_required
def delete_card(request, user_card_id):
    if request.method == 'POST':
        CardCRUDService.delete_card(user_card_id, request.user)
        return redirect('my_cards')

    card = get_object_or_404(Card, user=request.user, user_card_id=user_card_id)
    return render(request, 'cardspage/confirm_card_delete.html', {'card': card})


@login_required
def quiz_start(request):
    context = QuizService.build_quiz_start_context(request.user)
    return render(request, 'cardspage/quiz_start.html', context)


@login_required
def quiz(request):
    if request.method == 'GET':
        context = QuizService.build_quiz_context(request.user, request.GET)
        return render(request, 'cardspage/quiz.html', context)
    return redirect('quiz_start')


@login_required
def quiz_results(request):
    if request.method == 'POST':
        context = QuizService.build_quiz_results_context(request.POST)
        return render(request, 'cardspage/quiz_results.html', context)
    return redirect('quiz_start')