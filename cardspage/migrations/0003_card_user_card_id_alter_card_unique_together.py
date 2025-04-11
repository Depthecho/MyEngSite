from django.db import migrations, models

def assign_user_card_ids(apps, schema_editor):
    Card = apps.get_model('cardspage', 'Card')
    from collections import defaultdict

    user_counters = defaultdict(int)

    for card in Card.objects.all().order_by('user_id', 'created_at'):
        user_counters[card.user_id] += 1
        card.user_card_id = user_counters[card.user_id]
        card.save()

class Migration(migrations.Migration):

    dependencies = [
        ('cardspage', '0002_remove_flashcard_category_remove_flashcard_user_card_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='card',
            name='user_card_id',
            field=models.PositiveIntegerField(null=True),
        ),
        migrations.RunPython(assign_user_card_ids),
        migrations.AlterField(
            model_name='card',
            name='user_card_id',
            field=models.PositiveIntegerField(),
        ),
        migrations.AlterUniqueTogether(
            name='card',
            unique_together={('user', 'user_card_id')},
        ),
    ]
