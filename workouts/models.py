from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Workouts(models.Model):
    title = models.CharField(max_length=200)
    exercise = models.CharField(max_length=100)
    weight = models.DecimalField(max_digits=4, decimal_places=2)
    reps = models.IntegerField()
    # sets = models.IntegerField()
    created = models.DateTimeField(auto_now_add=True)
