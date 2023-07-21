from django.http import HttpResponse
from .models import Flight, Booking
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login as auth_login
from django.contrib.auth.decorators import login_required
from django.urls import reverse
import uuid
import time
import datetime
from datetime import date, timedelta


def home(request):
    return render(request, 'home.html')

def login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            auth_login(request, form.get_user())
            return redirect('search_flights')
    else:
        form = AuthenticationForm()
        return render(request, 'login.html', {'form': form})

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(request, user)
            return redirect('search_flights')
        else:
            return render(request, 'signup.html', {'form': form})
    else:
        form = UserCreationForm()
        return render(request, 'signup.html', {'form': form})

@login_required
def bookings(request):
    bookings = Booking.objects.filter(user=request.user)
    context = {'bookings': bookings}
    return render(request, 'bookings.html', context)


def search_flights(request):
    airports = Flight.objects.values_list('departure_airport', 'arrival_airport').distinct()

    departure_airport = request.GET.get('departure_airport')
    arrival_airport = request.GET.get('arrival_airport')
    date = request.GET.get('date')

    flights = Flight.objects.filter(
        departure_airport=departure_airport,
        arrival_airport=arrival_airport,
        departure_date=date,
    )

    if flights:
        flight_list = []
        for flight in flights:
            url = reverse('book_flight', args=[flight.flightnumber])
            flight_dict = {'flight': flight, 'booking_url': url}
            flight_list.append(flight_dict)

        context = {
            'flight_list': flight_list,
            'departure_airport': departure_airport,
            'arrival_airport': arrival_airport,
            'date': date,
            'airports': airports,
        }

        return render(request, 'search_flights.html', context)
    else:
        context = {
            'no_flights': True,
            'departure_airport': departure_airport,
            'arrival_airport': arrival_airport,
            'date': date,
            'airports': airports,
        }

        return render(request, 'search_flights.html', context)


def generate_booking_id():
    while True:
        # Get the current timestamp in milliseconds
        timestamp = int(time.time() * 1000)

        # Generate a random 6-character string
        random_string = str(uuid.uuid4().hex)[:6]

        # Combine the timestamp and random string to form the booking ID
        booking_id = f"{timestamp}-{random_string}"

        print("Generated booking ID:", booking_id)

        return booking_id

def book_flight(request, flight_number):
    flight = get_object_or_404(Flight, flightnumber=flight_number)
    if request.method == 'POST':
        # Retrieve the passenger details from the request POST data
        name = request.POST.get('name')
        email = request.POST.get('email')
        seats = int(request.POST['seats'])


        print (flight.available_seats, seats)
        if int(seats) <= flight.available_seats:
            # Create a new booking object and save it to the database
            booking = Booking.objects.create(
                flight_number=flight,
                user=request.user,
                passenger_name=name,
                passenger_email=email,
                num_passengers=seats,
                booking_id=generate_booking_id(),
            )

            flight.available_seats -= seats
            flight.save()

            context = {'booking_id': booking.booking_id}
            return render(request, 'booking_confirmation.html', context)
        elif int(seats) > flight.available_seats:
            error_message = 'Enter a value less than or equal to the available seats shown below'
            print('error_message:', error_message)
            context = {'flight': flight, 'error_message': error_message}
            return render(request, 'book_flight.html', context)

    else:
        # Render the booking form template with the flight details
        context = {'flight': flight}
        return render(request, 'book_flight.html', context)
