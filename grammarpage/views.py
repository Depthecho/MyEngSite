from django.shortcuts import render, get_object_or_404, Http404
from .grammar_topics import grammar_topics_data

def grammar_list(request):
    return render(request, 'grammarpage/grammar_list.html', {
        'grammar_topics': grammar_topics_data
    })

def grammar_main_topic_detail(request, main_topic_slug):
    main_topic = None
    for topic in grammar_topics_data:
        if topic.get('slug') == main_topic_slug:
            main_topic = topic
            break

    if not main_topic:
        raise Http404("Main grammar topic not found")

    return render(request, 'grammarpage/grammar_topic_list.html', {
        'main_category': main_topic,
    })


def grammar_sub_topic_detail(request, main_topic_slug, sub_topic_slug):
    main_topic = None
    for topic in grammar_topics_data:
        if topic.get('slug') == main_topic_slug:
            main_topic = topic
            break

    if not main_topic:
        raise Http404("Main grammar topic not found")

    selected_sub_topic = None
    breadcrumbs_path = [
        {'title': main_topic['title'], 'slug': main_topic['slug']}
    ]

    def find_sub_topic_recursive(current_topics, target_slug, current_path):
        nonlocal selected_sub_topic
        for item in current_topics:
            new_path = current_path + [{'title': item['title'], 'slug': item.get('slug')}]
            if item.get('slug') == target_slug:
                selected_sub_topic = item
                return new_path
            if 'sub_topics' in item:
                found_path = find_sub_topic_recursive(item['sub_topics'], target_slug, new_path)
                if found_path:
                    return found_path
        return None

    if 'sub_topics' in main_topic:
        full_path_found = find_sub_topic_recursive(main_topic['sub_topics'], sub_topic_slug, breadcrumbs_path)
        if full_path_found:
            breadcrumbs_path = full_path_found

    if not selected_sub_topic:
        raise Http404("Grammar sub-topic not found")

    return render(request, 'grammarpage/grammar_sub_topic_detail.html', {
        'main_topic': main_topic,
        'topic': selected_sub_topic,
        'breadcrumbs_path': breadcrumbs_path
    })