# Generated by Django 4.2.5 on 2023-11-16 22:25

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("hrdata", "0003_document_region"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="document",
            name="content_LLM",
        ),
        migrations.RemoveField(
            model_name="document",
            name="content_html",
        ),
    ]