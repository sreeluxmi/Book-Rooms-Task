from django.urls import path
from .views import room_booking , BookingListView ,UpdateBooking,DeleteBooking

urlpatterns = [
    path('book_room/', room_booking, name="bookroom"),
    path('booked_rooms/' , BookingListView.as_view() , name='bookedrooms'),
    path('update_booking/<int:pk>/' , UpdateBooking.as_view(), name= "update_booking"),
    path('delete_booking/<int:pk>/' , DeleteBooking.as_view(), name= "delete_booking"),
]
