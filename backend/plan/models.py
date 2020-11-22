from django.db import models
from django.contrib.auth.models import User
from location.models import Location

class Plan(models.Model):
    author = models.ForeignKey(
        User,
        on_delete = models.CASCADE,
        related_name = 'author_uid',
        null = True,
    )
    destination = models.ForeignKey(
        Location,
        on_delete = models.CASCADE,
        related_name = 'destination_id',
        null = True,
    )
    duration = models.IntegerField(default=0)
    #duration = models.DurationField(null=True, blank =True) 
    keywords = models.TextField()
    like_cnt = models.IntegerField(default=0)
    gallery_thumbnail = models.ImageField(blank=True)
    #cover_img = models.ForeignKey()
# Create your models here.
