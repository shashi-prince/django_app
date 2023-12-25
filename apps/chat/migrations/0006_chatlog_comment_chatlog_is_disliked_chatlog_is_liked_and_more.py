# Generated by Django 4.2.5 on 2023-11-21 07:50

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("chat", "0005_remove_chatlog_user_chatlog_last_updated_by"),
    ]

    operations = [
        migrations.AddField(
            model_name="chatlog",
            name="comment",
            field=models.TextField(default=""),
        ),
        migrations.AddField(
            model_name="chatlog",
            name="is_disliked",
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name="chatlog",
            name="is_liked",
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name="chatlog",
            name="question",
            field=models.TextField(default=""),
            preserve_default=False,
        ),
    ]
