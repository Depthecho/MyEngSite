from django.shortcuts import render
from .models import Text
from .services import TextService
from django.shortcuts import render, get_object_or_404


def texts_page(request):
    page_obj = TextService.get_filtered_texts(request)
    params = TextService._extract_params(request)
    context = TextService.get_context(page_obj, params)
    return render(request, 'textspage/texts_page.html', context)

def text_detail(request, pk):
    text = get_object_or_404(Text, pk=pk)
    context = {
        'text': text
    }
    return render(request, 'textspage/text_detail.html', context)