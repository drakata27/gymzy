from django.contrib import admin

from . import models

# Register your models here.
class WorkoutsAdmin(admin.ModelAdmin):
    list_display = ('title',)

class ExerciseAdmin(admin.ModelAdmin):
    list_display = ('exercise','weight','reps', 'sets', 'created', 'workouts')

admin.site.register(models.Workouts, WorkoutsAdmin)
admin.site.register(models.Exercise, ExerciseAdmin)
