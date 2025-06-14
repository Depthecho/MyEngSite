document.addEventListener('DOMContentLoaded', function() {

    function getCookie(name) {
        let cookieValue = null;
        if (document.cookie && document.cookie !== '') {
            const cookies = document.cookie.split(';');
            for (let i = 0; i < cookies.length; i++) {
                const cookie = cookies[i].trim();
                if (cookie.substring(0, name.length + 1) === (name + '=')) {
                    cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                    break;
                }
            }
        }
        return cookieValue;
    }

    const translatorFab = document.getElementById('translatorFab');
    const translatorContainer = document.getElementById('translatorContainer');
    const closeTranslatorBtn = document.getElementById('closeTranslatorBtn');
    const translateButton = document.getElementById('translateButton');
    const textToTranslate = document.getElementById('textToTranslate');
    const sourceLang = document.getElementById('sourceLang');
    const targetLang = document.getElementById('targetLang');
    const translatedText = document.getElementById('translatedText');
    const errorMessage = document.getElementById('errorMessage');

    if (translatorFab) {
        translatorFab.addEventListener('click', function(event) {
            event.stopPropagation();
            translatorContainer.classList.toggle('hidden');
            translatorContainer.classList.toggle('visible');
        });
    }

    if (closeTranslatorBtn) {
        closeTranslatorBtn.addEventListener('click', function() {
            translatorContainer.classList.add('hidden');
            translatorContainer.classList.remove('visible');
        });
    }

    if (translateButton) {
        translateButton.addEventListener('click', async () => {
            const text = textToTranslate.value;
            const srcLang = sourceLang.value;
            const trgLang = targetLang.value;

            if (!text.trim()) {
                errorMessage.textContent = 'Пожалуйста, введите текст для перевода.';
                errorMessage.style.display = 'block';
                return;
            } else {
                errorMessage.style.display = 'none';
            }

            try {
                const response = await fetch('/api/translate/', {
                    method: 'POST',
                    headers: {
                        'Content-Type': 'application/json',
                        'X-CSRFToken': getCookie('csrftoken') || (typeof CSRF_TOKEN !== 'undefined' ? CSRF_TOKEN : ''),
                    },
                    body: JSON.stringify({
                        text: text,
                        source_lang: srcLang,
                        target_lang: trgLang
                    })
                });

                const data = await response.json();

                if (response.ok) {
                    translatedText.value = data.translated_text;
                    errorMessage.style.display = 'none';
                } else {
                    translatedText.value = '';
                    errorMessage.textContent = data.error || 'Произошла ошибка перевода.';
                    errorMessage.style.display = 'block';
                }
            } catch (error) {
                console.error('Ошибка при отправке запроса на перевод:', error);
                translatedText.value = '';
                errorMessage.textContent = 'Не удалось соединиться с сервером перевода.';
                errorMessage.style.display = 'block';
            }
        });
    }

    const scrollToTopBtn = document.getElementById('scrollToTopBtn');

    window.addEventListener('scroll', () => {
        if (scrollToTopBtn) {
            if (window.scrollY > 300) {
                scrollToTopBtn.classList.add('visible');
                scrollToTopBtn.classList.remove('hidden');
            } else {
                scrollToTopBtn.classList.remove('visible');
                scrollToTopBtn.classList.add('hidden');
            }
        }
    });

    if (scrollToTopBtn) {
        scrollToTopBtn.addEventListener('click', () => {
            window.scrollTo({
                top: 0,
                behavior: 'smooth'
            });
        });
    }

    document.addEventListener('click', function(event) {
        if (translatorContainer && translatorContainer.classList.contains('visible') &&
            translatorFab && !translatorFab.contains(event.target) &&
            !translatorContainer.contains(event.target)) {
            translatorContainer.classList.add('hidden');
            translatorContainer.classList.remove('visible');
        }
    });

    if (translatorContainer) {
        translatorContainer.addEventListener('click', function(event) {
            event.stopPropagation();
        });
    }
});