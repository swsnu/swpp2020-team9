from django.db import models
from location.models import Location

class Reco_img(models.Model):
    image = models.ImageField(null = True)
    location = models.ForeignKey(
        Location,
        on_delete = models.CASCADE,
        related_name = 'location',
        null = True,
    )
    tags = models.TextField()

# Create your models here.
