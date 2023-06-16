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

    # def __init__(self, *args, **kwargs):      
    #     super().__init__(*args, **kwargs)
    #     if not self.instance.pk:
    #         date = self.data.get('date')
    #         available_rooms= Room.objects.exclude(
    #             roombooking__date=date,
    #             roombooking__start_time__lte=time(hour=9, minute=0),
    #             roombooking__end_time__gte=time(hour=18, minute=0)
    #         )
    #         if not available_rooms.exists():
    #              self.fields['room_name'].choices = [('', 'No room available')]



    
   

    

    













    




   







