# Generated by Django 5.0.7 on 2024-07-25 14:04

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("main", "0018_alter_tutorials_tutorial_published"),
    ]

    operations = [
        migrations.AlterField(
            model_name="tutorials",
            name="tutorial_published",
            field=models.DateTimeField(
                default=datetime.datetime(2024, 7, 25, 19, 34, 22, 533929),
                verbose_name="date published",
            ),
        ),
    ]
