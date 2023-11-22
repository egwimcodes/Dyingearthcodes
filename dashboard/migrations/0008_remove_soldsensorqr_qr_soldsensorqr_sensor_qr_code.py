# Generated by Django 4.2.2 on 2023-11-17 10:16

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("dashboard", "0007_soldsensorqr_qr"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="soldsensorqr",
            name="qr",
        ),
        migrations.AddField(
            model_name="soldsensorqr",
            name="sensor_qr_code",
            field=models.CharField(blank=True, max_length=30, null=True, unique=True),
        ),
    ]
