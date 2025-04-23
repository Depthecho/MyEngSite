from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from urllib.parse import urlencode
from .models import Card
from .forms import CardForm, QuizSettingsForm, QuizAnswerForm
from .services import CardQueryService, CardCRUDService, QuizService


@login_required
def my_cards(request: HttpRequest) -> HttpResponse:
    """Display user's cards with filtering and pagination options."""
    context = CardQueryService.build_my_cards_context(request.user, request.GET)
    return render(request, 'cardspage/my_cards.html', context)


@login_required
def add_cards(request: HttpRequest) -> HttpResponse:
    """Handle adding new cards."""
    form = CardForm(request.POST or None)

    if request.method == 'POST' and form.is_valid():
        CardCRUDService.create_card(form, request.user)
        return redirect('add_cards' if 'add_another' in request.POST else 'my_cards')

    context = {
        'form': form,
        'recent_cards': CardQueryService.get_recent_cards(request.user)
    }
    return render(request, 'cardspage/add_cards.html', context)


@login_required
def edit_card(request: HttpRequest, user_card_id: int) -> HttpResponse:
    """Handle editing existing cards."""
    card = get_object_or_404(Card, user=request.user, user_card_id=user_card_id)
    form = CardForm(request.POST or None, instance=card)

    if request.method == 'POST' and form.is_valid():
        CardCRUDService.update_card(form)
        return redirect('my_cards')

    return render(request, 'cardspage/edit_card.html', {'form': form, 'card': card})


@login_required
def delete_card(request: HttpRequest, user_card_id: int) -> HttpResponse:
    """Handle card deletion with preserved filter parameters."""
    preserved_params = {
        key: value
        for key, value in request.GET.items()
        if key in {'letter', 'sort', 'category', 'per_page', 'page'} and value
    }

    CardCRUDService.delete_card(user_card_id, request.user)

    base_url = reverse('my_cards')
    query_string = urlencode(preserved_params) if preserved_params else ''
    redirect_url = f"{base_url}?{query_string}" if query_string else base_url

    return redirect(redirect_url)


@login_required
def quiz_start(request: HttpRequest) -> HttpResponse:
    """Display quiz start page with statistics and options."""
    context = QuizService.build_quiz_start_context(request.user)
    return render(request, 'cardspage/quiz_start.html', context)


@login_required
def quiz(request: HttpRequest) -> HttpResponse:
    """Handle quiz generation and display."""
    if request.method == 'GET':
        form = QuizSettingsForm(request.GET)
        if form.is_valid():
            context = QuizService.build_quiz_context(
                request.user,
                form.cleaned_data
            )
            return render(request, 'cardspage/quiz.html', context)
    return redirect('quiz_start')


@login_required
def quiz_results(request: HttpRequest) -> HttpResponse:
    """Process quiz answers and display results."""
    if request.method == 'POST':
        context = QuizService.build_quiz_results_context(request.POST)
        return render(request, 'cardspage/quiz_results.html', context)
    return redirect('quiz_start')