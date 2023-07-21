from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator
from django.utils import timezone
from datetime import time
from datetime import date

class Flight(models.Model):
    flightnumber = models.CharField(max_length=10, primary_key=True, default="AA 201")
    departure_airport = models.CharField(max_length=50, default="")
    arrival_airport = models.CharField(max_length=50, default="")
    departure_date = models.DateField(default="2023-07-07")
    departure_time = models.TimeField(default="00:00")
    available_seats = models.PositiveSmallIntegerField(default=0, validators=[MaxValueValidator(60)])

    def __str__(self):
        return f'{self.departure_airport} to {self.arrival_airport}'

class Booking(models.Model):
    booking_id = models.CharField(max_length=50, primary_key=True)
    flight_number = models.ForeignKey(Flight, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE, default="")
    passenger_name = models.CharField(max_length=50)
    passenger_email = models.EmailField()
    num_passengers = models.PositiveIntegerField(default=0)

    def __str__(self):
        return f'{self.user.username} booked flight {self.flight_number}'
