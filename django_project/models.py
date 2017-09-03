from django.db import models
from constants import WATER_PERIOD_CHOICES
import uuid


class Plant(models.Model):

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    created = models.DateTimeField(auto_now_add=True, db_index=True)
    modified = models.DateTimeField(auto_now=True)
    name = models.CharField(max_length=500)
    water_period = models.CharField(
        choices=WATER_PERIOD_CHOICES,
        max_length=255,
        verbose_name='Watering Period'
    )

    class Meta:
        ordering = ["-created"]
