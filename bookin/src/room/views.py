from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.contrib import messages
<<<<<<< HEAD
from django.views.generic import ListView, UpdateView, DeleteView
from .models import RoomBooking
from .forms import RoomBookingForm
=======
from django.views.generic import ListView,UpdateView,DeleteView


from .models import *
from .forms import *

# Create your views here.
>>>>>>> a2717e46caaea4230ab7a26309028879c5aa10c9


def room_booking(request):

    if request.method == "POST":
        form = RoomBookingForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('bookroom')
    else:
        form = RoomBookingForm()  
<<<<<<< HEAD
=======

    
    return render(request, 'booking.html', {'form': form })

>>>>>>> a2717e46caaea4230ab7a26309028879c5aa10c9

    return render(request, 'booking.html', {'form': form})

class BookingListView(ListView):
    model = RoomBooking
    context_object_name = "booked"
    template_name = 'booked.html'

class UpdateBooking(UpdateView):
    model = RoomBooking
<<<<<<< HEAD
    form_class = RoomBookingForm
    template_name = 'booking.html'
    success_url = reverse_lazy('bookedrooms')

class DeleteBooking(DeleteView):
    model = RoomBooking
    context_object_name = "booked"
    success_url = reverse_lazy('bookedrooms')
    template_name = 'booked.html'    
 
=======
    fields = '__all__'
    success_url = reverse_lazy('bookedrooms')
    template_name = 'booking.html'


class DeleteBooking(DeleteView):
    model = RoomBooking
    fields = '__all__'
    context_object_name = "booked"
    success_url = reverse_lazy('bookedrooms')
    template_name = 'booked.html'    
>>>>>>> a2717e46caaea4230ab7a26309028879c5aa10c9



