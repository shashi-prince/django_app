# Generated by Django 4.2.5 on 2023-11-21 15:09

import apps.chat.models
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("chat", "0009_rename_bookmark_chatlog_is_bookmarked"),
    ]

    operations = [
        migrations.AlterField(
            model_name="chatlog",
            name="id",
            field=models.BigIntegerField(
                default=apps.chat.models.generate_random_id,
                editable=False,
                primary_key=True,
                serialize=False,
            ),
        ),
    ]
