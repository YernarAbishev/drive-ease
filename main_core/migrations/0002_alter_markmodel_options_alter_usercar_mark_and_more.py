# Generated by Django 5.0.6 on 2024-06-04 19:10

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("main_core", "0001_initial"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="markmodel",
            options={"verbose_name": "Model", "verbose_name_plural": "Models"},
        ),
        migrations.AlterField(
            model_name="usercar",
            name="mark",
            field=models.CharField(max_length=100, verbose_name="Mark"),
        ),
        migrations.AlterField(
            model_name="usercar",
            name="model",
            field=models.CharField(max_length=100, verbose_name="Model"),
        ),
    ]
