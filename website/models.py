from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import User
import datetime


# Create your models here.
class Airport(models.Model):
    code = models.CharField(max_length=3)
    city = models.CharField(max_length=64)

    def __str__(self):
        return f"{self.city} ({self.code})"

class Flight(models.Model):
    origin = models.ForeignKey(Airport, on_delete=models.CASCADE, related_name="departures") #if airport is deleted from Airports, then flights referencing that airport also get deleted. If we have an airport we can access all of the "departures" from it.
    destination = models.ForeignKey(Airport, on_delete=models.CASCADE, related_name="arrivals")
    duration = models.IntegerField()

    def __str__(self):
        return f"{self.id}: {self.origin} to {self.destination}"

class Passenger(models.Model):
    first = models.CharField(max_length=64)
    last = models.CharField(max_length=64)
    flights = models.ManyToManyField(Flight, blank=True, related_name="passengers")
    # can use flights attribute to access all their flights, and if we have a flight we can use related_name "passengers" to see all the passengers.
    def __str__(self):
        return f"{self.first} {self.last}"

class Feeling(models.Model):
    feeling_options = models.CharField(max_length=15)

    def __str__(self):
        return f"{self.feeling_options}"

class Sleep(models.Model):
    sleep_options = models.CharField(max_length=15)

    def __str__(self):
        return f"{self.sleep_options}"

class Meals(models.Model):
    meals_options = models.CharField(max_length=20)

    def __str__(self):
        return f"{self.meals_options}"

class Meetings(models.Model):
    meetings_options = models.CharField(max_length=15)

    def __str__(self):
        return f"{self.meetings_options}"

class Mood(models.Model):
    username = models.CharField(max_length=64)
    date = models.DateTimeField(default=datetime.datetime.now())
    mood = models.ForeignKey(Feeling, on_delete=models.CASCADE, related_name="feeling")
    sleep = models.ForeignKey(Sleep, on_delete=models.CASCADE, related_name="sleep")
    meals = models.ForeignKey(Meals, on_delete=models.CASCADE, related_name="meals")
    meetings = models.ForeignKey(Meetings, on_delete=models.CASCADE, related_name="meetings")
    diary = models.TextField()



# class User(models.Model):
#     firstname = models.CharField(max_length=20)
#     lastname = models.CharField(max_length=20)
#     email = models.EmailField(max_length=30)
#     password = models.CharField(max_length=20)
#     country = models.CharField(max_length=20)

#     def __str__(self):
#         return f"{self.firstname} {self.lastname} is from {self.country}. His/her email is {self.email} and has the password {self.password}."