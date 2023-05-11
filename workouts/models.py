from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Workouts(models.Model):
    title = models.CharField(max_length=200)

    def __str__(self):
        return self.title

class Exercise(models.Model):
    exercise = models.CharField(max_length=100)
    weight = models.DecimalField(max_digits=5, decimal_places=2)
    reps = models.IntegerField()
    sets = models.IntegerField()
    created = models.DateTimeField(auto_now_add=True)
    workouts = models.ForeignKey(Workouts, on_delete=models.CASCADE)

    def __str__(self):
        return self.exercise
