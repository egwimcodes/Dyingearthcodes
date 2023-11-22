# Generated by Django 4.2.2 on 2023-11-17 09:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        (
            "dashboard",
            "0005_soldsensorqr_unsoldsensorqr_alter_payloads_humidity_and_more",
        ),
    ]

    operations = [
        migrations.RemoveField(
            model_name="soldsensorqr",
            name="sensor_qr",
        ),
        migrations.AlterField(
            model_name="soldsensorqr",
            name="sensor",
            field=models.OneToOneField(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="soldsensorqr_set",
                to="dashboard.sensor",
            ),
        ),
    ]
