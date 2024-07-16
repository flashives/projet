# Generated by Django 5.0.6 on 2024-06-21 11:41

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0007_remove_forumrepley_message_remove_forumrepley_user_and_more'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='lesson',
            name='createur',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='lesson',
            name='niveau',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='app.niveau'),
        ),
        migrations.AddField(
            model_name='lesson',
            name='slug',
            field=models.SlugField(default='default-slug'),
        ),
        migrations.AddField(
            model_name='matiere',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='matiere_photos/'),
        ),
        migrations.AddField(
            model_name='matiere',
            name='slug',
            field=models.SlugField(default='default-slug'),
        ),
        migrations.AddField(
            model_name='niveau',
            name='slug',
            field=models.SlugField(default='default-slug'),
        ),
    ]
