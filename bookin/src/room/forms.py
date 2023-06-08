from django import forms
from .models import *


class RoomBookingForm(forms.ModelForm):
    start_time = forms.TimeField(
        input_formats=['%H:%M'],
        widget=forms.TimeInput(format='%H:%M'),
    )
    end_time = forms.TimeField(
        input_formats=['%H:%M'],
        widget=forms.TimeInput(format='%H:%M'),
    )
    date = forms.DateField(
        input_formats=['%d/%m/%Y', '%Y-%m-%d'],
        widget=forms.DateInput(format='%d/%m/%Y')
        )
    
    class Meta:
        model = RoomBooking
        fields = "__all__"



