import logging
from functools import wraps
from django.contrib import messages
from django.shortcuts import redirect

logger = logging.getLogger(__name__)

def handle_errors(view_func):
    @wraps(view_func)
    def wrapper(request, *args, **kwargs):
        try:
            return view_func(request, *args, **kwargs)
        except Exception as e:
            logger.error(f'Error in {view_func.__name__}: {e}', exc_info=True)
            messages.error(request, 'An error occurred. Please try again.')
            return redirect('home')
    return wrapper