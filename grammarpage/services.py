from typing import Dict, List, Optional


class GrammarService:
    def __init__(self, grammar_data: List[Dict]):
        self.grammar_data = grammar_data

    def get_main_topic(self, slug: str) -> Optional[Dict]:
        return next((topic for topic in self.grammar_data if topic.get('slug') == slug), None)

    def get_sub_topic_with_breadcrumbs(self, main_slug: str, sub_slug: str) -> tuple:
        main_topic = self.get_main_topic(main_slug)
        if not main_topic:
            return None, None, None

        breadcrumbs = [{'title': main_topic['title'], 'slug': main_topic['slug']}]

        def find_recursive(topics, target_slug, path):
            for item in topics:
                current_path = path + [{'title': item['title'], 'slug': item.get('slug')}]
                if item.get('slug') == target_slug:
                    return item, current_path
                if 'sub_topics' in item:
                    found, found_path = find_recursive(item['sub_topics'], target_slug, current_path)
                    if found:
                        return found, found_path
            return None, None

        sub_topic, full_breadcrumbs = find_recursive(main_topic.get('sub_topics', []), sub_slug, breadcrumbs)
        return main_topic, sub_topic, full_breadcrumbs