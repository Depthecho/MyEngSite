from django.core.paginator import Paginator
from typing import Any, Dict, List, Optional, Tuple, Union
import random
from .models import Card
from django.db.models.query import QuerySet
from django.forms import Form
from django.contrib.auth.models import AbstractUser
from mainpage.models import CustomUser

CustomUser = CustomUser

class CardFilterService:
    @staticmethod
    def apply_filters(queryset: QuerySet[Card], filters: Dict[str, Any]) -> QuerySet[Card]:
        """Применяет все фильтры к queryset"""
        queryset = CardFilterService._apply_letter_filter(queryset, filters.get('letter'))
        queryset = CardFilterService._apply_category_filter(queryset, filters.get('category'))
        queryset = CardFilterService._apply_sort(queryset, filters.get('sort'))
        return queryset

    @staticmethod
    def _apply_letter_filter(queryset: QuerySet[Card], letter: Optional[str]) -> QuerySet[Card]:
        if letter and letter.lower() != 'all':
            return queryset.filter(english_word__istartswith=letter)
        return queryset

    @staticmethod
    def _apply_category_filter(queryset: QuerySet[Card], category: Optional[str]) -> QuerySet[Card]:
        if category:
            if category == 'uncategorized':
                return queryset.filter(category__isnull=True)
            return queryset.filter(category=category)
        return queryset

    @staticmethod
    def _apply_sort(queryset: QuerySet[Card], sort: Optional[str]) -> QuerySet[Card]:
        if sort == 'oldest':
            return queryset.order_by('created_at')
        return queryset.order_by('-created_at')


class CardQueryService:
    @staticmethod
    def get_user_cards(user: CustomUser, **filters: Any) -> QuerySet[Card]:
        """Основной метод для получения карточек с фильтрами"""
        queryset: QuerySet[Card] = Card.objects.filter(user=user)
        return CardFilterService.apply_filters(queryset, filters)

    @staticmethod
    def get_recent_cards(user: CustomUser, limit: int = 12) -> QuerySet[Card]:
        return CardQueryService.get_user_cards(user, sort='newest')[:limit]

    @staticmethod
    def get_user_categories(user: CustomUser) -> QuerySet[str]:
        return Card.objects.filter(user=user).exclude(
            category__isnull=True
        ).order_by('category').values_list('category', flat=True).distinct()

    @staticmethod
    def build_my_cards_context(user: CustomUser, get_params: Dict[str, Any]) -> Dict[str, Any]:
        params: Dict[str, Any] = {
            'letter': get_params.get('letter', '').upper(),
            'sort': get_params.get('sort', 'newest'),
            'category': get_params.get('category'),
            'per_page': int(get_params.get('per_page', 16)),
            'page_number': get_params.get('page', 1)
        }

        queryset: QuerySet[Card] = CardQueryService.get_user_cards(user, **params)
        paginator: Paginator = Paginator(queryset, params['per_page'])
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
    def create_card(form: Form, user: CustomUser) -> Card:
        card: Card = form.save(commit=False)
        card.user = user
        card.save()
        return card

    @staticmethod
    def update_card(form: Form) -> None:
        form.save()

    @staticmethod
    def delete_card(user_card_id: int, user: CustomUser) -> bool:
        try:
            card: Card = Card.objects.get(user_card_id=user_card_id, user=user)
            card.delete()
            return True
        except Card.DoesNotExist:
            return False
        except Exception:
            return False


class QuestionBuilder:
    @staticmethod
    def create_question(
        card: Card,
        direction: str,
        mode: str,
        all_cards: List[Card]
    ) -> Dict[str, Any]:
        question: str
        correct_answer: str
        question, correct_answer = QuestionBuilder._get_question_data(card, direction)

        return {
            'id': card.id,
            'question': question,
            'correct_answer': correct_answer,
            'answers': QuestionBuilder._get_wrong_answers(card, direction, all_cards) + [correct_answer]
            if mode == 'multiple_choice' else None
        }

    @staticmethod
    def _get_question_data(card: Card, direction: str) -> Tuple[str, str]:
        if direction == 'en_to_native':
            return (card.english_word, card.native_translation)
        return (card.native_translation, card.english_word)

    @staticmethod
    def _get_wrong_answers(
        card: Card,
        direction: str,
        all_cards: List[Card]
    ) -> List[str]:
        return [
            c.native_translation if direction == 'en_to_native' else c.english_word
            for c in random.sample([c for c in all_cards if c != card], min(3, len(all_cards) - 1))
        ]


class QuizResultProcessor:
    @staticmethod
    def process_answers(post_data: Dict[str, Any]) -> Dict[str, Any]:
        mode: str = post_data.get('mode', 'multiple_choice')
        answers: Dict[str, Dict[str, Any]] = {}
        correct: int = 0

        for key, user_answer in post_data.items():
            if key.startswith('question_'):
                question_id: str = key.split('_')[1]
                correct_answer: str = post_data.get(f'correct_answer_{question_id}', '')

                is_correct: bool = QuizService._check_answer(user_answer, correct_answer, mode)

                answers[question_id] = {
                    'user_answer': user_answer,
                    'correct_answer': correct_answer,
                    'is_correct': is_correct
                }

                if is_correct:
                    correct += 1

        total: int = len(answers)
        return {
            'answers': answers,
            'correct': correct,
            'total': total,
            'percentage': round((correct / total) * 100) if total > 0 else 0,
            'mode': mode
        }


class QuizService:
    @staticmethod
    def build_quiz_start_context(user: CustomUser) -> Dict[str, Any]:
        categories: QuerySet[str] = Card.get_user_categories(user)
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
    def build_quiz_context(
        user: CustomUser,
        get_params: Dict[str, Any]
    ) -> Dict[str, Any]:
        params: Dict[str, Any] = {
            'direction': get_params.get('direction', 'en_to_native'),
            'category': get_params.get('category'),
            'mode': get_params.get('mode', 'multiple_choice'),
            'limit': QuizService._parse_limit(get_params.get('limit'))
        }

        questions: List[Dict[str, Any]] = QuizService._generate_questions(user, **params)
        return {
            'questions': questions,
            'mode': params['mode'],
            'direction': params['direction']
        }

    @staticmethod
    def build_quiz_results_context(post_data: Dict[str, Any]) -> Dict[str, Any]:
        return QuizResultProcessor.process_answers(post_data)

    @staticmethod
    def _parse_limit(limit: Optional[str]) -> Optional[int]:
        try:
            return int(limit) if limit and limit != 'all' else None
        except ValueError:
            return None

    @staticmethod
    def _generate_questions(
        user: CustomUser,
        direction: str,
        category: Optional[str],
        limit: Optional[int],
        mode: str
    ) -> List[Dict[str, Any]]:
        queryset: QuerySet[Card] = Card.objects.filter(user=user)
        if category:
            queryset = queryset.filter(category=category)

        cards: List[Card] = list(queryset)
        random.shuffle(cards)
        cards = cards[:limit] if limit else cards

        return [
            QuestionBuilder.create_question(card, direction, mode, cards)
            for card in cards
        ]

    @staticmethod
    def _check_answer(user_answer: str, correct_answer: str, mode: str) -> bool:
        if mode == 'spelling':
            return user_answer.strip().lower() == correct_answer.strip().lower()
        return user_answer == correct_answer