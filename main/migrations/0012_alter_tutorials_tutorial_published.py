# Generated by Django 5.0.7 on 2024-07-24 11:13

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0011_alter_tutorials_tutorial_published'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tutorials',
            name='tutorial_published',
            field=models.DateTimeField(default=datetime.datetime(2024, 7, 24, 16, 43, 15, 336552), verbose_name='date published'),
        ),
    ]
