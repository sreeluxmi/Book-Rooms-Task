from django.urls import path
from .views import room_booking , BookingListView

urlpatterns = [
    path('book_room/', room_booking, name="bookroom"),
    path('booked_rooms/' , BookingListView.as_view() , name='bookedrooms')
]
