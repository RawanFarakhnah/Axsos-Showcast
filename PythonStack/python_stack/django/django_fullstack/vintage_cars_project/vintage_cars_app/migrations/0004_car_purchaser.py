# Generated by Django 4.2.20 on 2025-03-17 22:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('vintage_cars_app', '0003_remove_car_purchasers'),
    ]

    operations = [
        migrations.AddField(
            model_name='car',
            name='purchaser',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='purchas_cars', to='vintage_cars_app.user'),
        ),
    ]
