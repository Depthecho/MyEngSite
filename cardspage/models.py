from django.db import models
from mainpage.models import CustomUser

class Card(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    user_card_id = models.PositiveIntegerField(default=0)
    english_word = models.CharField(max_length=100)
    native_translation = models.CharField(max_length=100)
    category = models.CharField(max_length=50, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('user', 'user_card_id')

    def __str__(self):
        return f"{self.english_word} -> {self.native_translation}"

    def save(self, *args, **kwargs):
        if not self.user_card_id:
            last_card = Card.objects.filter(user=self.user).order_by('-user_card_id').first()
            self.user_card_id = (last_card.user_card_id + 1) if last_card else 1
        super().save(*args, **kwargs)

    @classmethod
    def get_user_categories(cls, user):
        return cls.objects.filter(user=user).exclude(category__isnull=True).values_list('category',
                                                                                        flat=True).distinct()