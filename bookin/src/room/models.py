from datetime import time
from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

# Create your models here.


class RoomBooking(models.Model):
    team_name = models.CharField(max_length=300)
    meeting_title = models.CharField(max_length=300)
    date = models.DateField()
    ROOM_CHOICES = [
        ('Room 1', 'room 1'),
        ('Room 2', 'room 2'),
    ]
    room_number = models.CharField(max_length=100, choices=ROOM_CHOICES) 
    start_time = models.TimeField(
    validators=[
        MinValueValidator(time(hour=9, minute=0)),
        MaxValueValidator(time(hour=18, minute=0))
    ]
    )
    end_time = models.TimeField(
    validators=[
        MinValueValidator(time(hour=9, minute=0)),
        MaxValueValidator(time(hour=18, minute=0))
    ]
    )

    def __str__(self):
        return self.team_name

