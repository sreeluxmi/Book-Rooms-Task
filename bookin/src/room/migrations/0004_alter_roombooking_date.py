# Generated by Django 4.0.3 on 2023-06-07 15:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('room', '0003_roombooking_room_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='roombooking',
            name='date',
            field=models.DateField(),
        ),
    ]