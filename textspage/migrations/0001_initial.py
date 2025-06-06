# Generated by Django 5.1.6 on 2025-05-30 16:29

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Text',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Title')),
                ('content', models.TextField(verbose_name='Content')),
                ('length', models.PositiveIntegerField(default=0, editable=False, verbose_name='Length')),
                ('english_level', models.CharField(choices=[('A0', 'A0'), ('A1', 'A1'), ('A2', 'A2'), ('B1', 'B1'), ('B2', 'B2'), ('C1', 'C1'), ('C2', 'C2')], max_length=2, verbose_name='English Level')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created At')),
                ('added_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='texts', to=settings.AUTH_USER_MODEL, verbose_name='Added By')),
            ],
            options={
                'verbose_name': 'Text',
                'verbose_name_plural': 'Texts',
                'ordering': ('-created_at',),
            },
        ),
    ]
