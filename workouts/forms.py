from django import forms

from .models import Workouts

class WorkoutsForm(forms.ModelForm):
    class Meta:
        model = Workouts
        fields = ('title', 'exercise', 'weight', 'reps', 'sets')
    widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control my-5'}),
            'exercise': forms.TextInput(attrs={'class': 'form-control mb5'}),
            'weight': forms.NumberInput(attrs={'class': 'form-control mb5'}),
            'reps': forms.NumberInput(attrs={'class': 'form-control mb5'}),
            'sets': forms.NumberInput(attrs={'class': 'form-control mb5'}),
        }