# Generated by Django 4.2.2 on 2023-07-17 14:38

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("dashboard", "0006_alter_todoapp_done"),
    ]

    operations = [
        migrations.AlterField(
            model_name="todoapp",
            name="time",
            field=models.DateTimeField(
                blank=True,
                default=datetime.datetime(2023, 7, 17, 15, 38, 37, 359421),
                null=True,
            ),
        ),
    ]
