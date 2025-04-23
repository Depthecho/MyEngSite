from django.core.paginator import Paginator
import random
from .models import Card


class CardFilterService:
    @staticmethod
    def apply_filters(queryset, filters):
        """Применяет все фильтры к queryset"""
        queryset = CardFilterService._apply_letter_filter(queryset, filters.get('letter'))
        queryset = CardFilterService._apply_category_filter(queryset, filters.get('category'))
        queryset = CardFilterService._apply_sort(queryset, filters.get('sort'))
        return queryset

    @staticmethod
    def _apply_letter_filter(queryset, letter):
        if letter and letter.lower() != 'all':
            return queryset.filter(english_word__istartswith=letter)
        return queryset

    @staticmethod
    def _apply_category_filter(queryset, category):
        if category:
            if category == 'uncategorized':
                return queryset.filter(category__isnull=True)
            return queryset.filter(category=category)
        return queryset

    @staticmethod
    def _apply_sort(queryset, sort):
        if sort == 'oldest':
            return queryset.order_by('created_at')
        return queryset.order_by('-created_at')


class CardQueryService:
    @staticmethod
    def get_user_cards(user, **filters):
        """Основной метод для получения карточек с фильтрами"""
        queryset = Card.objects.filter(user=user)
        return CardFilterService.apply_filters(queryset, filters)

    @staticmethod
    def get_recent_cards(user, limit=12):
        return CardQueryService.get_user_cards(user, sort='newest')[:limit]

    @staticmethod
    def get_user_categories(user):
        return Card.objects.filter(user=user).exclude(
            category__isnull=True
        ).order_by('category').values_list('category', flat=True).distinct()

    @staticmethod
    def build_my_cards_context(user, get_params):
        params = {
            'letter': get_params.get('letter', '').upper(),
            'sort': get_params.get('sort', 'newest'),
            'category': get_params.get('category'),
            'per_page': int(get_params.get('per_page', 16)),
            'page_number': get_params.get('page', 1)
        }

        queryset = CardQueryService.get_user_cards(user, **params)
        paginator = Paginator(queryset, params['per_page'])
        page_obj = paginator.get_page(params['page_number'])

        return {
            'page_obj': page_obj,
            'active_letter': params['letter'],
            'active_category': params['category'],
            'sort_order': params['sort'],
            'per_page': params['per_page'],
            'letters': [chr(i) for i in range(65, 91)] + ['ALL'],
            'categories': CardQueryService.get_user_categories(user)
        }


class CardCRUDService:
    @staticmethod
    def create_card(form, user):
        card = form.save(commit=False)
        card.user = user
        card.save()
        return card

    @staticmethod
    def update_card(form):
        form.save()

    @staticmethod
    def delete_card(user_card_id, user):
        try:
            card = Card.objects.get(user_card_id=user_card_id, user=user)
            card.delete()
            return True
        except Card.DoesNotExist:
            return False
        except Exception:
            return False


class QuestionBuilder:
    @staticmethod
    def create_question(card, direction, mode, all_cards):
        question, correct_answer = QuestionBuilder._get_question_data(card, direction)

        return {
            'id': card.id,  # Используем card.id
            'question': question,
            'correct_answer': correct_answer,
            'answers': QuestionBuilder._get_wrong_answers(card, direction, all_cards) + [correct_answer]
            if mode == 'multiple_choice' else None
        }

    @staticmethod
    def _get_question_data(card, direction):
        if direction == 'en_to_native':
            return (card.english_word, card.native_translation)
        return (card.native_translation, card.english_word)

    @staticmethod
    def _get_wrong_answers(card, direction, all_cards):
        return [
            c.native_translation if direction == 'en_to_native' else c.english_word
            for c in random.sample([c for c in all_cards if c != card], min(3, len(all_cards) - 1))
        ]


class QuizResultProcessor:
    @staticmethod
    def process_answers(post_data: dict) -> dict:
        mode = post_data.get('mode', 'multiple_choice')
        answers = {}
        correct = 0

        for key, user_answer in post_data.items():
            if key.startswith('question_'):
                question_id = key.split('_')[1]
                correct_answer = post_data.get(f'correct_answer_{question_id}', '')

                is_correct = QuizService._check_answer(user_answer, correct_answer, mode)

                answers[question_id] = {
                    'user_answer': user_answer,
                    'correct_answer': correct_answer,
                    'is_correct': is_correct
                }

                if is_correct:
                    correct += 1

        total = len(answers)
        return {
            'answers': answers,
            'correct': correct,
            'total': total,
            'percentage': round((correct / total) * 100) if total > 0 else 0,
            'mode': mode
        }


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
        return {
            'questions': questions,
            'mode': params['mode'],
            'direction': params['direction']
        }

    @staticmethod
    def build_quiz_results_context(post_data):
        return QuizResultProcessor.process_answers(post_data)

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
            QuestionBuilder.create_question(card, direction, mode, cards)
            for card in cards
        ]

    @staticmethod
    def _check_answer(user_answer, correct_answer, mode):
        if mode == 'spelling':
            return user_answer.strip().lower() == correct_answer.strip().lower()
        return user_answer == correct_answer