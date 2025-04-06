from .models import Card

class CardService:
    @staticmethod
    def get_user_cards(user, limit=None):
        """Получает карточки пользователя с возможностью ограничения количества"""
        queryset = Card.objects.filter(user=user).order_by('-created_at')
        return queryset[:limit] if limit else queryset

    @staticmethod
    def create_card(form, user):
        """Создает новую карточку для пользователя"""
        card = form.save(commit=False)
        card.user = user
        card.save()
        return card

    @staticmethod
    def get_card_for_user(card_id, user):
        """Безопасно получает карточку пользователя или возвращает 404"""
        return Card.objects.get(id=card_id, user=user)