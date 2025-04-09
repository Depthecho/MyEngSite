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