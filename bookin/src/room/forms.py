from django import forms
from .models import *

class DateInput(forms.DateInput):
    input_type = 'date'

class RoomBookingForm(forms.ModelForm):
    class Meta:
        model = RoomBooking
        fields = "__all__"
        widgets = {
            'date': DateInput(),
        }
        date = forms.DateField(
        widget=forms.DateInput(format='%m/%d/%Y'))

    def clean(self):
        cleaned_data = super().clean()
        room_name = cleaned_data.get('room_name')
        date = cleaned_data.get('date')
        start_time = cleaned_data.get('start_time')
        end_time = cleaned_data.get('end_time')

        if room_name and date and start_time and end_time:
            conflicting_bookings = RoomBooking.objects.filter(
                room_name= room_name,
                date=date,
                start_time__lte=end_time,
                end_time__gte=start_time
            )

            fully_booked_rooms = Room.objects.filter(
                roombooking__date=date,
                roombooking__start_time__lte=time(hour=9, minute=0),
                roombooking__end_time__gte=time(hour=18, minute=0)
            )

            if room_name in fully_booked_rooms:
                self.fields['room_name'].queryset = fully_booked_rooms.exclude(id=room_name.id)

            if conflicting_bookings.exists():
                raise forms.ValidationError("This room is already booked for the selected time.")

        return cleaned_data

    
   

    

    













    




   







