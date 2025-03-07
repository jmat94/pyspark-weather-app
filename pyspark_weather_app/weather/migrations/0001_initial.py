# Generated by Django 5.1.6 on 2025-03-02 01:50

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Weather",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("city", models.CharField(max_length=100)),
                ("temperature", models.FloatField()),
                ("humidity", models.FloatField()),
                ("wind_speed", models.FloatField()),
                ("description", models.CharField(max_length=255)),
            ],
        ),
    ]
