# Generated by Django 5.0.6 on 2024-06-20 13:19

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0006_remove_lesson_evaluation_forummessage_forumrepley'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='forumrepley',
            name='message',
        ),
        migrations.RemoveField(
            model_name='forumrepley',
            name='user',
        ),
        migrations.AddField(
            model_name='lesson',
            name='evaluation',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='app.evaluation'),
        ),
        migrations.DeleteModel(
            name='ForumMessage',
        ),
        migrations.DeleteModel(
            name='ForumRepley',
        ),
    ]
