# Generated by Django 5.1.6 on 2025-05-30 15:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('profilepage', '0005_profile_english_level'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='english_level',
        ),
    ]
