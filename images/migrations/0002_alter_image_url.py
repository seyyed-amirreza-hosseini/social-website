# Generated by Django 5.0.8 on 2024-08-21 14:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("images", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="image",
            name="url",
            field=models.URLField(),
        ),
    ]
