from datetime import time
from django.db import models
from django.db.models import Q
from django.core.validators import MinValueValidator, MaxValueValidator
from django.forms import ValidationError

# Create your models here.



class Room(models.Model):
    room_number = models.CharField(max_length=60)

    def __str__(self):
        return self.room_number

class RoomBooking(models.Model):
    room_name = models.ForeignKey(Room , on_delete=models.CASCADE )
    team_name = models.CharField(max_length=300)
    meeting_title = models.CharField(max_length=300)
    date = models.DateField()
    

    start_time = models.TimeField(
        validators=[
            MinValueValidator(time(9, 0, 0)),
            MaxValueValidator(time(18, 0, 0))
        ]
    )

    end_time = models.TimeField(
        validators=[
            MinValueValidator(time(9, 0, 0)), 
            MaxValueValidator(time(18, 0, 0))
        ]
    )


    def __str__(self):
        return self.team_name
    


    


    

