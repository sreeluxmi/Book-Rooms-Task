from django.shortcuts import render
from .models import *
from .forms import *
from django.views.generic import ListView

# Create your views here.

def room_booking(request):
    form = RoomBookingForm()
    if request.method == "POST":
        form = RoomBookingForm(request.POST)
        if form.is_valid():   
            form.save()
        form = RoomBookingForm()
    return render(request, 'booking.html',{'form':form}) 


class BookingListView(ListView):
    model = RoomBooking
    context_object_name = "booked"
    template_name = 'booked.html'

