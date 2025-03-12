import random
from datetime import datetime, timedelta

from django.core.mail import send_mail
from django.conf import settings
from django.core.cache import cache

def generate_code():
    """Генерирует 6-значный код."""
    return str(random.randint(100000, 999999))

def can_send_code(email):
    """
    Проверяет, можно ли отправить код.
    Возвращает True, если прошло больше минуты с последней отправки.
    """
    last_sent_time = cache.get(f'last_sent_{email}')
    if last_sent_time:
        # Преобразуем строку времени обратно в объект datetime
        last_sent_time = datetime.fromisoformat(last_sent_time)
        if datetime.now() - last_sent_time < timedelta(minutes=1):
            return False
    return True

def send_verification_code(email):
    """Отправляет код на email и сохраняет его в Redis."""
    # Проверяем, можно ли отправить код
    if not can_send_code(email):
        return False, "Пожалуйста, подождите минуту перед повторной отправкой."

    # Генерируем новый код
    code = generate_code()

    # Сохраняем код в Redis с TTL 5 минут (300 секунд)
    cache.set(email, code, timeout=300)

    # Сохраняем время последней отправки в Redis с TTL 1 минута (60 секунд)
    cache.set(f'last_sent_{email}', datetime.now().isoformat(), timeout=60)

    # Отправляем email
    subject = 'Your verification code'
    message = f'Your verification code: {code}. The code is valid for 5 minutes.'
    send_mail(subject, message, settings.EMAIL_HOST_USER, [email])

    return True, "Код отправлен на ваш email."