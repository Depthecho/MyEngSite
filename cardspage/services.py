from django.core.paginator import Paginator
from django.core.exceptions import PermissionDenied
import random

from .models import Card


class CardQueryService:
    @staticmethod
    def get_user_cards(user, **filters):
        queryset = Card.objects.filter(user=user)
        return CardQueryService._apply_filters(queryset, **filters)

    @staticmethod
    def get_recent_cards(user, limit=12):
        return CardQueryService.get_user_cards(user, sort='newest', limit=limit)

    @staticmethod
    def build_my_cards_context(user, get_params):
        params = {
            'letter': get_params.get('letter', '').upper(),
            'sort': get_params.get('sort', 'newest'),
            'per_page': int(get_params.get('per_page', 16)),
            'page_number': get_params.get('page', 1)
        }

        queryset = CardQueryService.get_user_cards(user, **params)
        paginator = Paginator(queryset, params['per_page'])
        page_obj = paginator.get_page(params['page_number'])

        return {
            'page_obj': page_obj,
            'active_letter': params['letter'],
            'sort_order': params['sort'],
            'per_page': params['per_page'],
            'letters': [chr(i) for i in range(65, 91)] + ['ALL']
        }

    @staticmethod
    def _apply_filters(queryset, letter=None, sort='newest', **kwargs):
        if letter and letter.lower() != 'all':
            queryset = queryset.filter(english_word__istartswith=letter)

        if sort == 'oldest':
            queryset = queryset.order_by('created_at')
        else:
            queryset = queryset.order_by('-created_at')

        return queryset


class CardCRUDService:
    @staticmethod
    def create_card(form, user):
        card = form.save(commit=False)
        card.user = user
        card.save()
        return card

    @staticmethod
    def delete_card(card_id, user):
        card = Card.objects.filter(id=card_id, user=user).first()
        if not card:
            raise PermissionDenied("Card not found or permission denied")
        card.delete()


class QuizService:
    @staticmethod
    def build_quiz_start_context(user):
        categories = Card.get_user_categories(user)
        return {
            'categories': categories,
            'card_counts': {
                'total': Card.objects.filter(user=user).count(),
                'by_category': {
                    category: Card.objects.filter(user=user, category=category).count()
                    for category in categories
                }
            }
        }

    @staticmethod
    def build_quiz_context(user, get_params):
        params = {
            'direction': get_params.get('direction', 'en_to_native'),
            'category': get_params.get('category'),
            'mode': get_params.get('mode', 'multiple_choice'),
            'limit': QuizService._parse_limit(get_params.get('limit'))
        }

        questions = QuizService._generate_questions(user, **params)
        return {**params, 'questions': questions}

    @staticmethod
    def build_quiz_results_context(post_data):
        answers = {}
        correct = total = 0
        mode = post_data.get('mode', 'multiple_choice')

        for key, value in post_data.items():
            if key.startswith('question_'):
                question_id = key.split('_')[1]
                correct_answer = post_data.get(f'correct_answer_{question_id}')
                is_correct = QuizService._check_answer(value, correct_answer, mode)

                answers[question_id] = {
                    'user_answer': value,
                    'correct_answer': correct_answer,
                    'is_correct': is_correct
                }

                correct += is_correct
                total += 1

        return {
            'answers': answers,
            'correct': correct,
            'total': total,
            'mode': mode,
            'percentage': round((correct / total) * 100) if total > 0 else 0
        }

    @staticmethod
    def _parse_limit(limit):
        try:
            return int(limit) if limit and limit != 'all' else None
        except ValueError:
            return None

    @staticmethod
    def _generate_questions(user, direction, category, limit, mode):
        queryset = Card.objects.filter(user=user)
        if category:
            queryset = queryset.filter(category=category)

        cards = list(queryset)
        random.shuffle(cards)
        cards = cards[:limit] if limit else cards

        return [
            QuizService._create_question(card, direction, mode, cards)
            for card in cards
        ]

    @staticmethod
    def _create_question(card, direction, mode, all_cards):
        if direction == 'en_to_native':
            question = card.english_word
            correct_answer = card.native_translation
        else:
            question = card.native_translation
            correct_answer = card.english_word

        if mode == 'spelling':
            return {
                'id': card.id,
                'question': question,
                'correct_answer': correct_answer
            }

        wrong_answers = [
            c.native_translation if direction == 'en_to_native' else c.english_word
            for c in random.sample([c for c in all_cards if c != card], min(3, len(all_cards) - 1))
        ]

        return {
            'id': card.id,
            'question': question,
            'answers': random.sample(wrong_answers + [correct_answer], len(wrong_answers) + 1),
            'correct_answer': correct_answer
        }

    @staticmethod
    def _check_answer(user_answer, correct_answer, mode):
        if mode == 'spelling':
            return user_answer.strip().lower() == correct_answer.strip().lower()
        return user_answer == correct_answer