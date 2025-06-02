from django.shortcuts import render, redirect, get_object_or_404
from .models import Text
from .services import TextService


def texts_page(request):
    page_obj = TextService.get_filtered_texts(request)
    params = TextService._extract_params(request)
    context = TextService.get_context(page_obj, params)
    return render(request, 'textspage/texts_page.html', context)


def text_detail(request, pk):
    text = get_object_or_404(Text, pk=pk)

    if request.method == 'POST' and request.user.is_authenticated:
        TextService.mark_as_read(pk, request.user)
        return redirect('text_detail', pk=pk)

    context = {
        'text': text,
        'is_read': request.user.is_authenticated and text.read_by.filter(id=request.user.id).exists()
    }
    return render(request, 'textspage/text_detail.html', context)