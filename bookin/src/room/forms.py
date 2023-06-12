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
   
    def clean(self):
        avail_list =[]
        cleaned_data = super().clean()
        room_number = cleaned_data.get('room_number')
        date = cleaned_data.get('date')
        start_time = cleaned_data.get('start_time')
        end_time = cleaned_data.get('end_time')

        if room_number and date and start_time and end_time:
            not_available_bookings = RoomBooking.objects.filter(
                room_number=room_number,
                date=date,
                start_time__lte=end_time,
                end_time__gte=start_time
            )

            if not_available_bookings.exists():
                raise forms.ValidationError("This room is already booked.")
 
        return cleaned_data





