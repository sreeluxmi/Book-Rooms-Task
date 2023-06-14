from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.contrib import messages
from django.views.generic import ListView, UpdateView, DeleteView
from .models import RoomBooking
from .forms import RoomBookingForm

def room_booking(request):
    if request.method == "POST":
        form = RoomBookingForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('bookroom')
    else:
        form = RoomBookingForm()  

    return render(request, 'booking.html', {'form': form})

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
 



