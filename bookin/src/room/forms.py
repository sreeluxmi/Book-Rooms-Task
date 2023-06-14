from django import forms
from .models import Room, RoomBooking
from datetime import time


class DateInput(forms.DateInput):
    input_type = 'date'

class RoomBookingForm(forms.ModelForm):
    class Meta:
        model = RoomBooking
        fields = "__all__"
        widgets = {
            'date': DateInput(),
        }

    def __init__(self, *args, **kwargs):      
        super().__init__(*args, **kwargs)
        if not self.instance.pk:
            date = self.data.get('date')
            self.fields['room_name'].queryset = Room.objects.exclude(
                roombooking__date=date,
                roombooking__start_time__lte=time(hour=9, minute=0),
                roombooking__end_time__gte=time(hour=18, minute=0)
            ) 

    def clean(self):
        cleaned_data = super().clean()
        room = cleaned_data.get('room_name')
        date = cleaned_data.get('date')
        start_time = cleaned_data.get('start_time')
        end_time = cleaned_data.get('end_time')

        if room and date and start_time and end_time:
            not_available_room = RoomBooking.objects.filter(
                room_name=room,
                date=date,
                start_time__lt=end_time,
                end_time__gt=start_time
            )

            if not_available_room.exists():
                raise forms.ValidationError("This room is already booked for this time.")

        return cleaned_data








    
   

    

    













    




   







