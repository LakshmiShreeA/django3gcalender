# Generated by Django 4.1.3 on 2023-02-18 08:26

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0004_task_desc_task_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='start_date',
            field=models.DateField(default=datetime.date.today),
        ),
    ]
