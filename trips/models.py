from django.core.validators import MinLengthValidator, MinValueValidator
from django.db import models
from travelers.models import Traveler

class Trip(models.Model):
    destination = models.CharField(max_length=100, validators=[MinLengthValidator(3)])
    summary = models.TextField()
    start_date = models.DateField()
    duration = models.PositiveSmallIntegerField(
        default=1, validators=[MinValueValidator(1)], help_text="*Duration in days is expected."
    )
    image_url = models.URLField(blank=True, null=True)
    traveler = models.ForeignKey(Traveler, on_delete=models.CASCADE, related_name="trips")

    def __str__(self):
        return self.destination