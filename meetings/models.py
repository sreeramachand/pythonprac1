from django.db import models
from datetime import time 
from django.contrib.auth import get_user_model

class Room(models.Model):
    name = models.CharField(max_length=50)
    floor = models.IntegerField()
    room_number = models.IntegerField()

    def __str__(self):
        return f"Room {self.name} is at door {self.room_number} on floor {self.floor}"

# Create your models here.
class Meeting(models.Model):
    title = models.CharField(max_length=200)
    date = models.DateField()
    start_time = models.TimeField(default=time(9))
    duration = models.IntegerField(default=1)
    room = models.ForeignKey(Room, on_delete=models.CASCADE) #Creates a ForeignKey relation from the Meeting class to the Room Class. This field will hold the ID of the room object that this meeting references. If this room is deleted, then all meetings for that room will also be deleted. 
    participants = models.ManyToManyField(get_user_model())

    def __str__(self):
        return f"{self.title} at {self.start_time} on {self.date}"