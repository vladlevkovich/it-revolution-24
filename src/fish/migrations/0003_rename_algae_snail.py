# Generated by Django 5.0.4 on 2024-04-14 07:43

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('fish', '0002_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Algae',
            new_name='Snail',
        ),
    ]
