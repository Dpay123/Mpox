# Generated by Django 4.0.4 on 2022-08-19 18:31

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_alter_task_compdate_alter_task_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2022, 8, 19, 18, 31, 39, 192772)),
        ),
    ]