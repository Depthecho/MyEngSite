from django.conf import settings
from typing import Optional, Dict, Any


class TranslationService:

    def __init__(self):
        self._translator = self._initialize_translator()

    @staticmethod
    def _initialize_translator():
        try:
            from lara_sdk import Translator, Credentials
            credentials = Credentials(
                settings.LARA_ACCESS_KEY_ID,
                settings.LARA_ACCESS_KEY_SECRET
            )
            return Translator(credentials=credentials)
        except ImportError as e:
            raise ImportError("Lara SDK не установлен. Установите: pip install lara-sdk") from e
        except Exception as e:
            raise Exception(f"Ошибка инициализации Lara SDK: {str(e)}") from e

    def translate(
            self,
            text: str,
            target_lang: str = 'en',
            source_lang: Optional[str] = None
    ) -> str:

        if not text:
            raise ValueError("Не предоставлен текст для перевода")

        if not self._translator:
            raise RuntimeError("Сервис перевода не инициализирован")

        params: Dict[str, Any] = {
            'text': text,
            'target': target_lang
        }
        if source_lang and source_lang != 'auto':
            params['source'] = source_lang

        response = self._translator.translate(**params)
        if not response or not hasattr(response, 'translation'):
            raise ValueError("Неверный формат ответа от сервиса перевода")

        return response.translation