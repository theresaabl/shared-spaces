from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField


class EventSpace(models.Model):
    name = models.CharField(max_length=200, unique=True)
    type = models.CharField(max_length=200)
    image = CloudinaryField('image', default='placeholder')
    building = models.CharField(max_length=200)
    capacity = models.PositiveSmallIntegerField()
    number_of_tables = models.PositiveSmallIntegerField()
    number_of_chairs = models.PositiveSmallIntegerField()
    kitchen = models.BooleanField()
    tea_and_coffeemaker = models.BooleanField()
    projector = models.BooleanField()
    audio_equipment = models.BooleanField()
    childrens_play_area = models.BooleanField()
    piano = models.BooleanField()
    notes = models.TextField(blank=True)
