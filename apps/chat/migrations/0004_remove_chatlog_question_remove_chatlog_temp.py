# Generated by Django 4.2.5 on 2023-11-18 07:15

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("chat", "0003_rename_context_chatlog_model_name_chatlog_prompt"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="chatlog",
            name="question",
        ),
        migrations.RemoveField(
            model_name="chatlog",
            name="temp",
        ),
    ]
