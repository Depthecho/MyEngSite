import random
import json
from datetime import timedelta
from django.utils import timezone
from django.db.models import F
from django.shortcuts import get_object_or_404
from profilepage.models import Profile, Notification
from testspage.models import UserTestResult, EnglishLevelTest
from testspage.data.level_test_questions import LEVEL_TEST_QUESTIONS

# Константы для ключей сессии
SESSION_QUESTIONS_ORDER_KEY = 'level_test_questions_order'
SESSION_TEST_ANSWERS_KEY = 'test_answers'


class TestAvailabilityService:
    """Сервис проверки доступности теста для пользователя"""
    MIN_STREAK_DAYS = 10
    TEST_COOLDOWN_DAYS = 10

    @classmethod
    def check_availability(cls, user_profile):
        if user_profile.streak < cls.MIN_STREAK_DAYS:
            return (
                f"To take the English level test, you need at least a {cls.MIN_STREAK_DAYS}-day streak. "
                f"Your current streak: {user_profile.streak}."
            )

        last_completion = UserTestResult.objects.filter(
            user=user_profile.user,
            english_level_determined__isnull=False
        ).order_by('-completed_at').first()

        if last_completion and (timezone.now() - last_completion.completed_at).days < cls.TEST_COOLDOWN_DAYS:
            days_left = cls.TEST_COOLDOWN_DAYS - (timezone.now() - last_completion.completed_at).days
            return f"You can retake the test in {days_left} days."

        return None


class QuestionService:
    """Сервис работы с вопросами теста"""

    @staticmethod
    def get_all_questions():
        """Получение всех вопросов"""
        return list(LEVEL_TEST_QUESTIONS)

    @staticmethod
    def get_shuffled_question_ids():
        """Получение перемешанных ID вопросов"""
        all_questions = QuestionService.get_all_questions()
        question_ids = [q['id'] for q in all_questions]
        random.shuffle(question_ids)
        return question_ids

    @staticmethod
    def get_questions_by_ids(question_ids):
        """Получение вопросов по списку ID"""
        questions_map = {q['id']: q for q in LEVEL_TEST_QUESTIONS}
        return [questions_map[q_id] for q_id in question_ids if q_id in questions_map]


class TestEvaluationService:
    """Сервис оценки результатов теста"""

    @staticmethod
    def evaluate_answers(user_answers, all_questions):
        """
        Оценка ответов пользователя
        Возвращает: (user_score, total_score, percentage)
        """
        questions_map = {q['id']: q for q in all_questions}
        user_score = 0
        total_score = sum(q['points'] for q in all_questions)

        for question_key, user_answer in user_answers.items():
            if not question_key.startswith('question_'):
                continue

            try:
                question_id = int(question_key.split('_')[1])
            except (ValueError, IndexError):
                continue

            question = questions_map.get(question_id)
            if not question:
                continue

            if question['type'] == 'multiple_choice':
                if TestEvaluationService._check_multiple_choice(question, user_answer):
                    user_score += question['points']
            elif question['type'] == 'text_input':
                if TestEvaluationService._check_text_input(question, user_answer):
                    user_score += question['points']

        percentage = (user_score / total_score) * 100 if total_score > 0 else 0
        return user_score, total_score, percentage

    @staticmethod
    def _check_multiple_choice(question, user_answer):
        """Проверка ответа с множественным выбором"""
        try:
            selected_id = int(user_answer)
            return any(a['id'] == selected_id and a['is_correct']
                       for a in question['answers'])
        except (ValueError, TypeError):
            return False

    @staticmethod
    def _check_text_input(question, user_answer):
        """Проверка текстового ответа"""
        user_answer_lower = str(user_answer).strip().lower()
        return any(keyword.lower() in user_answer_lower
                   for keyword in question.get('keywords', []))


class LevelDeterminationService:
    """Сервис определения уровня английского"""

    LEVEL_THRESHOLDS = {
        'C2': 90,
        'C1': 80,
        'B2': 65,
        'B1': 50,
        'A2': 30,
        'A1': 15,
        'A0': 0
    }

    @staticmethod
    def determine_level(percentage):
        """Определение уровня по проценту правильных ответов"""
        for level, threshold in LevelDeterminationService.LEVEL_THRESHOLDS.items():
            if percentage >= threshold:
                return level
        return 'A0'


class TestResultService:
    """Сервис работы с результатами теста"""

    @staticmethod
    def save_test_result(user, score, max_score, percentage, level, questions_count):
        """Сохранение результатов теста"""
        test_instance = EnglishLevelTest.objects.get_or_create(
            title="Comprehensive Level Test",
            defaults={'description': "System-generated level test", 'is_active': False}
        )[0]

        result = UserTestResult.objects.create(
            user=user,
            test=test_instance,
            score=score,
            total_questions=questions_count,
            max_possible_score=max_score,
            percentage=percentage,
            english_level_determined=level,
            completed_at=timezone.now()
        )

        TestResultService._update_user_profile(user)
        TestResultService._create_notification(user, result, score, max_score, percentage)

        return result

    @staticmethod
    def _update_user_profile(user):
        """Обновление профиля пользователя"""
        user.profile.tests_completed = F('tests_completed') + 1
        user.profile.save()
        user.profile.refresh_from_db()
        user.profile.check_achievements()

    @staticmethod
    def _create_notification(user, test_result, score, max_score, percentage):
        """Создание уведомления о результате"""
        message = (
            f"You completed the English level test. "
            f"Score: {score}/{max_score} ({percentage:.1f}%). "
            f"Your level: {test_result.get_english_level_determined_display()}. "
            "Apply this level to your profile?"
        )
        Notification.objects.create(
            user=user,
            notification_type='SYSTEM',
            title='Level Test Completed!',
            message=message,
            content_object=test_result
        )

    @staticmethod
    def apply_level_to_profile(user, result_id):
        """Применение уровня к профилю пользователя"""
        result = get_object_or_404(UserTestResult, id=result_id, user=user)
        profile = user.profile
        profile.english_level = result.english_level_determined
        profile.save()

        Notification.objects.create(
            user=user,
            notification_type='SYSTEM',
            title='English Level Updated!',
            message=f"Your level is now {profile.get_english_level_display()}.",
        )
        return True