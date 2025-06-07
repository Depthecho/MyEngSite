from django.db import models
from django.conf import settings
from django.utils import timezone
from profilepage.models import Profile

class EnglishLevelTest(models.Model):
    title = models.CharField(max_length=255, verbose_name="Test Title")
    description = models.TextField(blank=True, verbose_name="Test Description")
    is_active = models.BooleanField(default=True, verbose_name="Is Active Test")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "English Level Test"
        verbose_name_plural = "English Level Tests"
        permissions = [
            ("can_view_english_level_test", "Can view English level test"),
        ]


class Question(models.Model):
    test = models.ForeignKey(
        EnglishLevelTest,
        on_delete=models.CASCADE,
        related_name='questions',
        verbose_name="Test"
    )
    text = models.TextField(verbose_name="Question Text")

    def __str__(self):
        return f"Question for '{self.test.title}': {self.text[:70]}..."

    class Meta:
        verbose_name = "Question"
        verbose_name_plural = "Questions" # Corrected from verbose_plural
        ordering = ['id']


class Answer(models.Model):
    question = models.ForeignKey(
        Question,
        on_delete=models.CASCADE,
        related_name='answers',
        verbose_name="Question"
    )
    text = models.CharField(max_length=255, verbose_name="Answer Text")
    is_correct = models.BooleanField(default=False, verbose_name="Is Correct")

    def __str__(self):
        return f"Answer to '{self.question.text[:50]}...': {self.text}"

    class Meta:
        verbose_name = "Answer"
        verbose_name_plural = "Answers"
        ordering = ['id']


class UserTestResult(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='test_results',
        verbose_name="User"
    )
    test = models.ForeignKey(
        EnglishLevelTest,
        on_delete=models.CASCADE,
        related_name='results',
        verbose_name="Test"
    )
    score = models.PositiveIntegerField(verbose_name="Score")
    total_questions = models.PositiveIntegerField(verbose_name="Total Questions")
    max_possible_score = models.PositiveIntegerField(default=0, verbose_name="Maximum Possible Score")
    percentage = models.FloatField(verbose_name="Correct Percentage")
    english_level_determined = models.CharField(
        max_length=2,
        choices=Profile.ENGLISH_LEVEL_CHOICES,
        blank=True,
        null=True,
        verbose_name="Determined English Level"
    )
    completed_at = models.DateTimeField(auto_now_add=True, verbose_name="Completion Date")
    last_level_test_completion = models.DateTimeField(
        null=True,
        blank=True,
        verbose_name="Last Level Test Completion"
    )

    def __str__(self):
        return f"Test result for '{self.test.title}' by {self.user.username}"

    class Meta:
        verbose_name = "User Test Result"
        verbose_name_plural = "User Test Results"
        ordering = ['-completed_at']