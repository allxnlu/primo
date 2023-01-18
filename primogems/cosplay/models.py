from django.db import models
from datetime import datetime

# Create your models here.
class CosEvent(models.Model):
    title = models.CharField(max_length=100)
    place = models.CharField(max_length=100)
    date = models.DateField()
    ongoing = models.BooleanField()

    def __str__(self):
        return f"{self.title} in {self.place} on {self.date}"
        
class Cosplay(models.Model):
    title = models.CharField(max_length=100)
    character = models.CharField(max_length=50)
    date = models.DateField()
    time_created = models.TimeField(default=datetime.now())
    no_images = models.ImageField(default=0)
    event = models.ForeignKey(CosEvent, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.title} - {self.character} on {self.date}"

