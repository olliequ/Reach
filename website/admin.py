from django.contrib import admin

from .models import Flight, Airport, Passenger, Mood, Feeling, Meetings, Meals, Sleep

# Register your models here.

class FlightAdmin(admin.ModelAdmin):
    list_display = ("id", "origin", "destination", "duration")

class PassengerAdmin(admin.ModelAdmin):
    filter_horizontal = ("flights",)

admin.site.register(Airport) #we want to use admin to manipulate these 2 models.
admin.site.register(Flight, FlightAdmin)
admin.site.register(Passenger, PassengerAdmin)
admin.site.register(Mood)
admin.site.register(Feeling)
admin.site.register(Meetings)
admin.site.register(Meals)   
admin.site.register(Sleep) 