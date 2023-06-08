from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.contrib import messages
from django.views.generic import ListView,UpdateView,DeleteView


from .models import *
from .forms import *

# Create your views here.


def room_booking(request):
    if request.method == "POST":
        form = RoomBookingForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('bookedrooms')
    else:
        form = RoomBookingForm()
    return render(request, 'booking.html', {'form': form})



class BookingListView(ListView):
    model = RoomBooking
    context_object_name = "booked"
    template_name = 'booked.html'

class UpdateBooking(UpdateView):
    model = RoomBooking
    fields = '__all__'
    success_url = reverse_lazy('bookedrooms')
    template_name = 'booking.html'


class DeleteBooking(DeleteView):
    model = RoomBooking
    fields = '__all__'
    context_object_name = "booked"
    success_url = reverse_lazy('bookedrooms')
    template_name = 'booked.html'    



