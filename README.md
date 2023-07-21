# Flight Bookings App

This App provides a simple interface for users and site admins to log in/sign up.

A user will be able to make flight bookings using this web app with a login, sign-up, search the available flights, make a booking and lets a user view all of their bookings.

An admin would be able to login and view, edit and delete all available Users, Bookings and Flights.

Appropriate field validations, authentication and authorization methods are also integrated in the Django back end.

## Tech Stack
This app is built using Django. It uses a SQL Lite DB for backend and HTML templates for front end. Page routings are done by creating views using the Django framework

## Future Development
Dockerizing the app will let anymore use this environment without any set up as everything comes in a Docker container. The local deployment of Docker by installing Docker and using a docker build command worked for the current Dockerfile and hence included in the repository.

### Usage

1. Clone this repository by executing the following command in a CLI
   ```
   git clone https://github.com/preethikankeyan/flight_bookings_project.git
   ```
2. Go to the project directory by doing `cd flight_booking_project`
3. Install virtualenv if you don't already have it installed and create a virtual environment in the project root
   ```
   virtualenv app_env
   ```
4. Activate your virtualenv with `source venv/bin/activate`
5. Install project dependencies with `pip install -r requirements.txt`

## To see the flight bookings web app:
Execute the following command,
```
python manage.py runserver
```

Now open your browser and visit [http://127.0.0.1:8000/admin](http://127.0.0.1:8000/admin). You should see the Django 
admin screen. If you go to [http://127.0.0.1:8000/index/](http://127.0.0.1:8000/) you should see the Home page of the App.

##Hosting
This app is hosted using Github and PythonAnywhere (https://www.pythonanywhere.com/).

You can access the app without doing any of the above steps by going to - https://preethikankeyan.pythonanywhere.com/
The admin page can be accessed here - https://preethikankeyan.pythonanywhere.com/admin/
