from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User, Group
from .models import Flight, Booking

admin.site.site_header = 'Flight booking site administration'
admin.site.index_title = 'Click on the Bookings button to view, edit and change all Bookings, Click on the Flights button to view, edit and change all Flights, Click on the Users button to view, edit and change all Users'

class FlightAdmin(admin.ModelAdmin):
    list_display = ('flightnumber', 'departure_airport', 'arrival_airport', 'departure_date', 'departure_time', 'available_seats')
    list_filter = ('departure_airport', 'arrival_airport', 'departure_date')
    search_fields = ('flightnumber', 'departure_airport', 'arrival_airport')

class BookingAdmin(admin.ModelAdmin):
    list_display = ('booking_id', 'flight_number', 'user', 'passenger_name', 'passenger_email', 'num_passengers')
    list_filter = ('flight_number', 'user')
    search_fields = ('booking_id', 'user__username', 'passenger_name', 'passenger_email')

class MyUserAdmin(UserAdmin):
    list_display = ('username', 'email', 'first_name', 'last_name', 'is_staff')
    list_filter = ('is_staff',)
    search_fields = ('username', 'email', 'first_name', 'last_name')

admin.site.unregister(User)
admin.site.unregister(Group)
admin.site.register(User, MyUserAdmin)
admin.site.register(Flight, FlightAdmin)
admin.site.register(Booking, BookingAdmin)
