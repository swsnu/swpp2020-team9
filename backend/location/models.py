from django.db import models

class Location(models.Model):
    name = models.CharField(max_length=63)
    latitude = models.FloatField(default=0)
    longitude = models.FloatField(default=0)

# Create your models here.
