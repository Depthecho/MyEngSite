from django import template
from ..models import Achievement

register = template.Library()


@register.inclusion_tag('profilepage/achievement_badge.html')
def show_achievement_badge(profile, badge_type, level, required_count):
    achieved = False
    higher_achieved = False

    # Проверяем текущий уровень
    current_achieved = Achievement.objects.filter(
        user=profile.user,
        badge_type=badge_type,
        level=level
    ).exists()

    # Проверяем более высокие уровни
    if level < 3:
        higher_achieved = Achievement.objects.filter(
            user=profile.user,
            badge_type=badge_type,
            level__gt=level
        ).exists()

    achieved = current_achieved or higher_achieved

    # Получаем текущее значение
    current_value = {
        'words': profile.words_learned,
        'texts': profile.texts_read,
        'tests': profile.tests_completed
    }.get(badge_type, 0)

    # Названия уровней
    level_names = {1: 'Bronze', 2: 'Silver', 3: 'Gold'}

    # Названия бейджей
    badge_names = {
        'words': {
            1: 'Word Collector',
            2: 'Word Expert',
            3: 'Word Master'
        },
        'texts': {
            1: 'Text Reader',
            2: 'Text Explorer',
            3: 'Text Scholar'
        },
        'tests': {
            1: 'Test Beginner',
            2: 'Test Challenger',
            3: 'Test Master'
        }
    }

    return {
        'badge_type': badge_type,
        'level': level,
        'level_name': level_names[level],
        'badge_name': badge_names[badge_type][level],
        'achieved': achieved,
        'higher_achieved': higher_achieved,
        'current_value': current_value,
        'required_value': required_count
    }