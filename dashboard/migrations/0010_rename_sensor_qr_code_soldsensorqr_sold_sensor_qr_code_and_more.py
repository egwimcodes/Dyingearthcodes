# Generated by Django 4.2.2 on 2023-11-17 10:19

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("dashboard", "0009_remove_unsoldsensorqr_sensor_qr_and_more"),
    ]

    operations = [
        migrations.RenameField(
            model_name="soldsensorqr",
            old_name="sensor_qr_code",
            new_name="sold_sensor_qr_code",
        ),
        migrations.RenameField(
            model_name="unsoldsensorqr",
            old_name="unsold_sensor_qr",
            new_name="unsold_sensor_qr_code",
        ),
    ]
