from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from .models import Text, TextCompletion
from .services import TextService


def texts_page(request):
    page_obj = TextService.get_filtered_texts(request)
    params = TextService._extract_params(request)
    context = TextService.get_context(page_obj, params)
    context['LANGUAGES'] = settings.LANGUAGES
    return render(request, 'textspage/texts_page.html', context)

@login_required
def text_detail(request, pk):
    text = get_object_or_404(Text, pk=pk)

    if request.method == 'POST' and request.user.is_authenticated:
        TextService.mark_as_read(pk, request.user)
        return redirect('text_detail', pk=pk)

    context = {
        'text': text,
        'is_read': request.user.is_authenticated and text.read_by.filter(id=request.user.id).exists(),
        'LANGUAGES': settings.LANGUAGES,
    }
    return render(request, 'textspage/text_detail.html', context)

@login_required
def complete_text(request, pk):
    text = get_object_or_404(Text, pk=pk)
    TextCompletion.objects.get_or_create(user=request.user, text=text)
    return redirect('texts_page')


@login_required
def completed_texts(request):
    # Получаем завершенные тексты для текущего пользователя
    completions = TextCompletion.objects.filter(user=request.user).select_related('text')
    completed_texts = [completion.text for completion in completions]

    # Используем тот же сервис для фильтрации и пагинации
    page_obj = TextService.get_filtered_texts(request, queryset=completed_texts)
    params = TextService._extract_params(request)
    context = TextService.get_context(page_obj, params)
    context['active_tab'] = 'completed'
    context['LANGUAGES'] = settings.LANGUAGES

    return render(request, 'textspage/completed_texts_page.html', context)