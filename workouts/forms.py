from django import forms

from .models import Workouts, Exercise

class WorkoutsForm(forms.ModelForm):
    class Meta:
        model = Workouts
        fields = ('title',)
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control my-5'}),
        }
    
class ExerciseForm(forms.ModelForm):
    class Meta:
        model = Exercise
        fields = ('exercise', 'weight', 'reps', 'sets','workouts')
        widgets = {
            'workouts': forms.HiddenInput(),
        }
        labels = {
            'weight' : 'Weight (kg)',
            'workouts' : 'This workout'
        }
