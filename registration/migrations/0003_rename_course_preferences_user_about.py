# Generated by Django 4.1.3 on 2023-05-26 03:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('registration', '0002_user_is_active'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='course_preferences',
            new_name='about',
        ),
    ]
