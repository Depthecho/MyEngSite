from django.shortcuts import render
from .services import TextService


def texts_page(request):
    page_obj = TextService.get_filtered_texts(request)
    params = TextService._extract_params(request)
    context = TextService.get_context(page_obj, params)
    return render(request, 'textspage/texts_page.html', context)