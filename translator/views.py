from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from .services import TranslationService


@csrf_exempt
def translate_text(request):
    if request.method != 'POST':
        return JsonResponse(
            {'error': 'Only POST requests are allowed.'},
            status=405
        )

    try:
        data = json.loads(request.body)
        service = TranslationService()

        translated_text = service.translate(
            text=data.get('text'),
            target_lang=data.get('target_lang', 'en'),
            source_lang=data.get('source_lang')
        )

        return JsonResponse({'translated_text': translated_text})

    except json.JSONDecodeError:
        return JsonResponse(
            {'error': 'Invalid JSON in request body.'},
            status=400
        )
    except ValueError as e:
        return JsonResponse(
            {'error': str(e)},
            status=400
        )
    except ImportError as e:
        return JsonResponse(
            {'error': 'Translation service unavailable.'},
            status=503
        )
    except Exception as e:
        return JsonResponse(
            {'error': f'Translation failed: {str(e)}'},
            status=500
        )