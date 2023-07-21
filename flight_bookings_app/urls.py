from django.urls import path, include

from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('book-flight/<str:flight_number>/', views.book_flight, name='book_flight'),
    path('book-flight/', views.book_flight, name='book_flight'),
    path('bookings/', views.bookings, name='bookings'),
    path('bookings/<str:flight_number>/', views.bookings, name='bookings'),
    path('login/', views.login, name='login'),
    path('signup/', views.signup, name='signup'),
    path('search-flights/', views.search_flights, name='search_flights'),
]

