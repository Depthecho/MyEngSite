from django.conf import settings
from django.shortcuts import render, Http404
from django.urls import reverse
from django.utils.translation import gettext_lazy as _

from .services import GrammarService
from .grammar_topics import grammar_topics_data

grammar_service = GrammarService(grammar_topics_data)

def grammar_list(request):
    return render(request, 'grammarpage3/grammar_list.html', {
        'grammar_topics': grammar_topics_data,
        'LANGUAGES': settings.LANGUAGES,
    })

def grammar_main_topic_detail(request, main_topic_slug):
    main_topic = grammar_service.get_main_topic(main_topic_slug)
    if not main_topic:
        raise Http404("Main grammar topic not found")

    return render(request, 'grammarpage3/grammar_topic_list.html', {
        'main_category': main_topic,
        'LANGUAGES': settings.LANGUAGES,
    })

def grammar_sub_topic_detail(request, main_topic_slug, sub_topic_slug):
    main_topic, sub_topic, breadcrumbs = grammar_service.get_sub_topic_with_breadcrumbs(
        main_topic_slug,
        sub_topic_slug
    )

    if not main_topic or not sub_topic:
        raise Http404("Grammar topic not found")

    return render(request, 'grammarpage3/grammar_sub_topic_detail.html', {
        'main_topic': main_topic,
        'topic': sub_topic,
        'breadcrumbs_path': breadcrumbs,
        'LANGUAGES': settings.LANGUAGES,
    })