# Generated by Django 5.0.1 on 2024-01-26 10:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapi', '0005_driver_userregistration_driverid_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='driver',
            name='bookingId',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='gettaxiform',
            name='bookingId',
            field=models.CharField(default=False, max_length=200),
        ),
    ]
