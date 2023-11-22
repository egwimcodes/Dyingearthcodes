# Generated by Django 4.2.2 on 2023-11-22 11:13

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        (
            "dashboard",
            "0010_rename_sensor_qr_code_soldsensorqr_sold_sensor_qr_code_and_more",
        ),
    ]

    operations = [
        migrations.AlterField(
            model_name="payloads",
            name="humidity",
            field=models.FloatField(default=0.0),
        ),
        migrations.AlterField(
            model_name="payloads",
            name="soil_moisture",
            field=models.FloatField(default=0.0),
        ),
        migrations.AlterField(
            model_name="payloads",
            name="temperature",
            field=models.FloatField(default=0.0),
        ),
        migrations.AlterField(
            model_name="soldsensorqr",
            name="sold_sensor_qr_code",
            field=models.CharField(blank=True, max_length=22, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name="unsoldsensorqr",
            name="unsold_sensor_qr_code",
            field=models.CharField(blank=True, max_length=22, null=True, unique=True),
        ),
    ]
