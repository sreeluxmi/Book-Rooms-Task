from datetime import time
from django.db import models
from django.db.models import CheckConstraint,Q,F
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
    
    class Meta:
        constraints = [
        CheckConstraint(
            check=Q(room_name__isnull=False) &
                  Q(date__isnull=False) &
                  Q(start_time__lt=F('end_time'))&
                  Q(end_time__gt=F('start_time')),
            name='check_room_booking'
        )]

   
    def clean(self):
        super().clean()
        if self.room_name and self.date and self.start_time and self.end_time:
            not_available_room = RoomBooking.objects.filter(
            Q(room_name=self.room_name),
            Q(date=self.date),
            Q(start_time__lt=self.end_time),
            Q(end_time__gt=self.start_time)
            )         

            if not_available_room.exists():
                raise ValidationError(("This room is already booked for this time."))



    

    


    

