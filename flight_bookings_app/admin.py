from django.contrib import admin
from .models import Flight, Booking

class FlightAdmin(admin.ModelAdmin):
    list_display = ('flightnumber', 'departure_airport', 'arrival_airport', 'departure_date', 'departure_time', 'available_seats')
    list_filter = ('departure_airport', 'arrival_airport', 'departure_date')
    search_fields = ('flightnumber', 'departure_airport', 'arrival_airport')

class BookingAdmin(admin.ModelAdmin):
    list_display = ('booking_id', 'flight_number', 'user', 'passenger_name', 'passenger_email', 'num_passengers')

admin.site.register(Flight, FlightAdmin)
admin.site.register(Booking, BookingAdmin)
