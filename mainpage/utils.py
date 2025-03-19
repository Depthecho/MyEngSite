import random
import logging
from datetime import datetime, timedelta
from django.core.mail import send_mail
from django.conf import settings
from django.core.cache import cache

logger = logging.getLogger(__name__)

CODE_SENT_SUCCESS_MSG = "Code was sent to your email."
CODE_SENT_TOO_SOON_MSG = "Please wait a minute before resending."

def generate_code():
    return str(random.randint(100000, 999999))

def can_send_code(email):
    last_sent_time = cache.get(f'last_sent_{email}')
    if last_sent_time and datetime.now() - last_sent_time < timedelta(minutes=1):
        return False
    return True

def save_code_to_cache(email, code):
    cache.set(email, code, timeout=300)
    logger.info(f"Code {code} cached for email {email}.")

def save_sent_time_to_cache(email):
    cache.set(f'last_sent_{email}', datetime.now(), timeout=60)
    logger.info(f"Sent time cached for email {email}.")

def send_email_with_code(email, code):
    subject = 'Your verification code'
    message = f'Your verification code: {code}. The code is valid for 5 minutes.'
    send_mail(subject, message, settings.EMAIL_HOST_USER, [email])

def send_verification_code(email):
    if not can_send_code(email):
        return False, CODE_SENT_TOO_SOON_MSG

    code = generate_code()
    save_code_to_cache(email, code)
    save_sent_time_to_cache(email)
    send_email_with_code(email, code)

    return True, CODE_SENT_SUCCESS_MSG