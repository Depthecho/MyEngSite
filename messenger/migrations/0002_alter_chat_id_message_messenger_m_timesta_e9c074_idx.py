import random
from django.conf import settings
from django.db import migrations, models

def generate_unique_chat_id(apps):
    """Генерирует уникальный 9-значный ID чата"""
    Chat = apps.get_model('messenger', 'Chat')
    while True:
        chat_id = random.randint(100_000_000, 999_999_999)  # 9 цифр
        if not Chat.objects.filter(id=chat_id).exists():
            return chat_id

def forwards_func(apps, schema_editor):
    """Заполняет случайными ID существующие чаты"""
    Chat = apps.get_model('messenger', 'Chat')
    for chat in Chat.objects.all():
        chat.id = generate_unique_chat_id(apps)
        chat.save()

def reverse_func(apps, schema_editor):
    """Обратная миграция - не требуется, так как автоинкрементные ID не восстанавливаем"""
    pass

class Migration(migrations.Migration):

    dependencies = [
        ('messenger', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AlterField(
            model_name='chat',
            name='id',
            field=models.BigIntegerField(editable=False, primary_key=True, serialize=False, unique=True, verbose_name='Chat ID'),
        ),
        migrations.RunPython(
            forwards_func,
            reverse_func,
        ),
        migrations.AddIndex(
            model_name='message',
            index=models.Index(fields=['timestamp'], name='messenger_m_timesta_e9c074_idx'),
        ),
    ]