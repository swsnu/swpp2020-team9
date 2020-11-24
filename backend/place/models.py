from django.db import models
from plan.models import Plan

class Place(models.Model):
    plan = models.ForeignKey(
        Plan,
        on_delete = models.CASCADE,
        related_name = 'plan_id',
        null = True,
    )
    latitude = models.FloatField(default=0)
    longitude = models.FloatField(default=0)
    name = models.CharField(max_length=63)
    rep_img = models.ImageField(blank=True)


# Create your models here.
