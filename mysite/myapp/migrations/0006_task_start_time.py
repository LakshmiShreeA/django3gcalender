# Generated by Django 4.1.3 on 2023-02-18 10:23

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0005_task_start_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='start_time',
            field=models.TimeField(default=datetime.time(10, 23, 42, 464052)),
        ),
    ]