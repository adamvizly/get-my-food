# Generated by Django 5.0.1 on 2024-01-03 12:08

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="DeliveryRequest",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                ("from_address", models.TextField()),
                ("to_address", models.TextField()),
                (
                    "attain_type",
                    models.IntegerField(choices=[(1, "Card"), (2, "Code")], default=2),
                ),
                ("code", models.CharField(blank=True, max_length=25, null=True)),
                ("delivery_time", models.DateTimeField(auto_now_add=True)),
                ("cost", models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name="Delivery",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                ("delivered_at", models.DateTimeField()),
                ("completed", models.BooleanField(default=False)),
                (
                    "request",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="getter.deliveryrequest",
                    ),
                ),
            ],
        ),
    ]
