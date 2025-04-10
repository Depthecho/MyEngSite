import random
from django.core.exceptions import PermissionDenied
from .models import Card

class CardService:
    @staticmethod
    def get_user_cards(user, limit=None):
        queryset = Card.objects.filter(user=user).order_by('-created_at')
        return queryset[:limit] if limit else queryset

    @staticmethod
    def create_card(form, user):
        card = form.save(commit=False)
        card.user = user
        card.save()
        return card

    @staticmethod
    def get_card_for_user(card_id, user):
        return Card.objects.get(id=card_id, user=user)

    @staticmethod
    def delete_card(card_id, user):
        """Удаляет карточку пользователя или вызывает PermissionDenied"""
        card = Card.objects.filter(id=card_id, user=user).first()
        if not card:
            raise PermissionDenied("The card was not found or you do not have permission to delete it.")
        card.delete()

    @staticmethod
    def get_quiz_questions(user, category=None, direction='en_to_native', limit=None):
        queryset = Card.objects.filter(user=user)
        if category:
            queryset = queryset.filter(category=category)

        cards = list(queryset)
        random.shuffle(cards)

        if limit:
            cards = cards[:limit]

        questions = []
        for card in cards:
            if direction == 'en_to_native':
                question = card.english_word
                correct_answer = card.native_translation
            else:
                question = card.native_translation
                correct_answer = card.english_word

            wrong_answers = [
                c.native_translation if direction == 'en_to_native' else c.english_word
                for c in random.sample(
                    [c for c in cards if c != card],
                    min(3, len(cards) - 1)
                )
            ]

            all_answers = wrong_answers + [correct_answer]
            random.shuffle(all_answers)

            questions.append({
                'id': card.id,
                'question': question,
                'answers': all_answers,
                'correct_answer': correct_answer
            })

        return questions