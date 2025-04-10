from django.db import models
from mainpage.models import CustomUser

class Card(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    english_word = models.CharField(max_length=100)
    native_translation = models.CharField(max_length=100)
    category = models.CharField(max_length=50, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.english_word} -> {self.native_translation}"

    @classmethod
    def get_user_categories(cls, user):
        return cls.objects.filter(user=user).exclude(category__isnull=True).values_list('category',
                                                                                        flat=True).distinct()