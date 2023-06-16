from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from datetime import time
from django.views.generic import ListView,UpdateView,DeleteView
from django.http import JsonResponse

from .models import *
from .forms import *

# Create your views here.

def room_booking(request):
    if request.method == "POST":
        form = RoomBookingForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('bookroom')
    else:
        form = RoomBookingForm()  

    if request.headers.get('x-requested-with') == 'XMLHttpRequest' and 'date' in request.GET:
        date = request.GET.get('date')
        start_time = time(hour=9, minute=0)
        end_time = time(hour=18, minute=0)
        booked_rooms = RoomBooking.objects.filter(date=date, end_time__gt=start_time, start_time__lt=end_time)
        available_rooms = Room.objects.exclude(roombooking__in=booked_rooms).values('id', 'room_number')

        for room in available_rooms:
            if room in booked_rooms:
                available_rooms.remove(room)

        if not available_rooms:
            message = "No rooms available."
        else:
            message = ""

        return JsonResponse({'rooms': list(available_rooms), 'message': message})  
    return render(request, 'booking.html', {'form': form })


    
class BookingListView(ListView):
    model = RoomBooking
    context_object_name = "booked"
    template_name = 'booked.html'

class UpdateBooking(UpdateView):
    model = RoomBooking
    form_class = RoomBookingForm
    template_name = 'booking.html'
    success_url = reverse_lazy('bookedrooms')

class DeleteBooking(DeleteView):
    model = RoomBooking
    context_object_name = "booked"
    success_url = reverse_lazy('bookedrooms')
    template_name = 'booked.html'      



