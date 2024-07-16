# Generated by Django 5.0.6 on 2024-06-27 22:37

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0008_lesson_createur_lesson_niveau_lesson_slug_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='lesson',
            name='evaluation',
        ),
        migrations.RemoveField(
            model_name='niveau',
            name='slug',
        ),
        migrations.AddField(
            model_name='niveau',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='niveau_photos/'),
        ),
        migrations.AlterField(
            model_name='lesson',
            name='matiere',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='lessons', to='app.matiere'),
        ),
    ]