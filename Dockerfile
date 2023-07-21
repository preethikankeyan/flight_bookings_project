FROM python:3-alpine3.15
RUN pip install --upgrade pip
WORKDIR /flight_bookings_app
COPY . /flight_bookings_app
RUN pip install -r requirement.txt
CMD ["python3","python manage.py", "runserver"]
