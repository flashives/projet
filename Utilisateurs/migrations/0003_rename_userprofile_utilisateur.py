# Generated by Django 5.0.6 on 2024-06-07 16:10

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Utilisateurs', '0002_userprofile_delete_utilisateur'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.RenameModel(
            old_name='UserProfile',
            new_name='utilisateur',
        ),
    ]
