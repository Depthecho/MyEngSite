import random
from django.core.mail import send_mail
from django.conf import settings
from django.core.cache import cache

def generate_code():
    """Генерирует 6-значный код."""
    return str(random.randint(100000, 999999))

def send_verification_code(email):
    """Отправляет код на email и сохраняет его в Redis."""
    # Генерируем новый код
    code = generate_code()

    # Сохраняем код в Redis с TTL 5 минут (300 секунд)
    cache.set(email, code, timeout=300)

    # Отправляем email
    subject = 'Your verification code'
    message = f'Your verification code: {code}. The code is valid for 5 minutes.'
    send_mail(subject, message, settings.EMAIL_HOST_USER, [email])