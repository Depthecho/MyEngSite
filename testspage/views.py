import json
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .services import (
    TestAvailabilityService,
    QuestionService,
    TestEvaluationService,
    LevelDeterminationService,
    TestResultService,
    SESSION_QUESTIONS_ORDER_KEY,
    SESSION_TEST_ANSWERS_KEY
)
from .models import UserTestResult


@login_required
def take_level_test(request):
    user_profile = request.user.profile

    # Проверка доступности теста
    availability_message = TestAvailabilityService.check_availability(user_profile)
    if availability_message:
        return render(request, 'testspage/test_unavailable.html', {
            'message': availability_message
        })

    # Инициализация теста в сессии
    if SESSION_QUESTIONS_ORDER_KEY not in request.session:
        shuffled_question_ids = QuestionService.get_shuffled_question_ids()
        request.session[SESSION_QUESTIONS_ORDER_KEY] = shuffled_question_ids
        request.session[SESSION_TEST_ANSWERS_KEY] = {}
        request.session.modified = True

    # Получение вопросов для текущей попытки
    question_ids = request.session[SESSION_QUESTIONS_ORDER_KEY]
    test_questions = QuestionService.get_questions_by_ids(question_ids)

    # Настройка пагинации
    questions_per_page = 10
    paginator = Paginator(test_questions, questions_per_page)

    # Обработка POST-запроса (ответы пользователя)
    if request.method == 'POST':
        if SESSION_TEST_ANSWERS_KEY not in request.session:
            request.session[SESSION_TEST_ANSWERS_KEY] = {}

        # Сохранение ответов текущей страницы
        current_page_number = request.POST.get('current_page_number')
        if current_page_number:
            try:
                current_page_number = int(current_page_number)
                for key, value in request.POST.items():
                    if key.startswith('question_'):
                        request.session[SESSION_TEST_ANSWERS_KEY][key] = value
                request.session.modified = True
            except (ValueError, TypeError):
                pass

        # Завершение теста
        if 'finish_test' in request.POST:
            final_answers = request.session.get(SESSION_TEST_ANSWERS_KEY, {})

            # Оценка результатов
            user_score, total_score, percentage = TestEvaluationService.evaluate_answers(
                final_answers, test_questions
            )

            # Определение уровня
            determined_level = LevelDeterminationService.determine_level(percentage)

            # Сохранение результата
            test_result = TestResultService.save_test_result(
                user=request.user,
                score=user_score,
                max_score=total_score,
                percentage=percentage,
                level=determined_level,
                questions_count=len(test_questions))

            # Очистка сессии
            if SESSION_QUESTIONS_ORDER_KEY in request.session:
                del request.session[SESSION_QUESTIONS_ORDER_KEY]
            if SESSION_TEST_ANSWERS_KEY in request.session:
                del request.session[SESSION_TEST_ANSWERS_KEY]

            return redirect('level_test_result', result_id=test_result.id)

        # Переход на следующую страницу
        else:
            next_page = request.POST.get('next_page_number')
            if next_page:
                return redirect(f"{request.path}?page={next_page}")
            return redirect(request.path_info)

    # Обработка GET-запроса (отображение страницы с вопросами)
    page_number = request.GET.get('page')
    try:
        current_page_questions = paginator.page(page_number)
    except PageNotAnInteger:
        current_page_questions = paginator.page(1)
    except EmptyPage:
        current_page_questions = paginator.page(paginator.num_pages)

    existing_answers = request.session.get(SESSION_TEST_ANSWERS_KEY, {})

    context = {
        'test': {
            'title': 'Comprehensive English Level Test',
        },
        'questions': current_page_questions,
        'is_demo_test': False,
        'paginator': paginator,
        'page_obj': current_page_questions,
        'existing_answers': json.dumps(existing_answers),
    }
    return render(request, 'testspage/english_level_test.html', context)


@login_required
def level_test_result(request, result_id):
    user_test_result = get_object_or_404(UserTestResult, id=result_id, user=request.user)
    profile = request.user.profile

    # Обработка POST-запросов (применение уровня или закрытие уведомления)
    if request.method == 'POST':
        action = request.POST.get('action')

        if action == 'apply_level':
            success = TestResultService.apply_level_to_profile(request.user, result_id)
            if success:
                return JsonResponse({'status': 'success', 'message': 'Level successfully applied.'})
            return JsonResponse({'status': 'error', 'message': 'Failed to apply level.'}, status=400)

        elif action == 'dismiss_notification':
            return JsonResponse({'status': 'success', 'message': 'Notification dismissed.'})

    # Проверка, применен ли уже уровень
    is_level_applied = (profile.english_level == user_test_result.english_level_determined)

    return render(request, 'testspage/test_result_notification.html', {
        'result': user_test_result,
        'current_level': profile.english_level,
        'is_level_applied': is_level_applied,
    })