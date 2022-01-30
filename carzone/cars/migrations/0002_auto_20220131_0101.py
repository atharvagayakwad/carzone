# Generated by Django 3.2.7 on 2022-01-30 19:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='carsmodel',
            name='doors',
            field=models.CharField(choices=[('2', '2'), ('3', '3'), ('4', '4'), ('5', '5'), ('6', '6')], max_length=10),
        ),
        migrations.AlterField(
            model_name='carsmodel',
            name='fuel_type',
            field=models.CharField(choices=[('Petrol', 'Petrol'), ('Diesel', 'Diesel'), ('CNG', 'CNG')], max_length=50),
        ),
        migrations.AlterField(
            model_name='carsmodel',
            name='is_featured',
            field=models.BooleanField(default=False),
        ),
    ]
