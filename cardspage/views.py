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

    recent_cards = CardService.get_user_cards(request.user, 12)
    return render(request, 'cardspage/add_cards.html', {
        'form': form,
        'recent_cards': recent_cards
    })


@login_required
def edit_card(request, user_card_id):
    card = get_object_or_404(Card, user=request.user, user_card_id=user_card_id)

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
def delete_card(request, user_card_id):
    if request.method == 'POST':
        CardService.delete_card(user_card_id, request.user)
        return redirect('my_cards')

    card = get_object_or_404(Card, user=request.user, user_card_id=user_card_id)
    return render(request, 'cardspage/confirm_card_delete.html', {'card': card})

@login_required
def quiz_start(request):
    categories = Card.get_user_categories(request.user)
    return render(request, 'cardspage/quiz_start.html', {
        'categories': categories,
        'card_counts': {
            'total': Card.objects.filter(user=request.user).count(),
            'by_category': {
                category: Card.objects.filter(user=request.user, category=category).count()
                for category in categories
            }
        }
    })


@login_required
def quiz(request):
    if request.method == 'GET':
        direction = request.GET.get('direction', 'en_to_native')
        category = request.GET.get('category')
        mode = request.GET.get('mode', 'multiple_choice')
        limit = request.GET.get('limit')

        try:
            limit = int(limit) if limit and limit != 'all' else None
        except ValueError:
            limit = None

        questions = CardService.get_quiz_questions(
            user=request.user,
            category=category,
            direction=direction,
            limit=limit
        )

        return render(request, 'cardspage/quiz.html', {
            'questions': questions,
            'direction': direction,
            'category': category,
            'limit': limit,
            'mode': mode
        })
    return redirect('quiz_start')


@login_required
@login_required
def quiz_results(request):
    if request.method == 'POST':
        answers = {}
        correct = 0
        total = 0
        mode = request.POST.get('mode', 'multiple_choice')

        for key, value in request.POST.items():
            if key.startswith('question_'):
                question_id = key.split('_')[1]
                correct_answer = request.POST.get(f'correct_answer_{question_id}')

                is_correct = value.strip().lower() == correct_answer.strip().lower() if mode == 'spelling' else value == correct_answer

                answers[question_id] = {
                    'user_answer': value,
                    'correct_answer': correct_answer,
                    'is_correct': is_correct
                }

                if is_correct:
                    correct += 1
                total += 1

        return render(request, 'cardspage/quiz_results.html', {
            'answers': answers,
            'correct': correct,
            'total': total,
            'mode': mode,
            'percentage': round((correct / total) * 100) if total > 0 else 0
        })

    return redirect('quiz_start')
