# Generated by Django 4.2.2 on 2023-06-13 09:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('room', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Room',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('room_number', models.CharField(max_length=60)),
            ],
        ),
        migrations.DeleteModel(
            name='RoomBooking',
        ),
    ]