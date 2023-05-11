from typing import Any, Dict
from django.urls import reverse
from django.db.models.query import QuerySet
from django.shortcuts import render
from django.views.generic import CreateView,DetailView, ListView, UpdateView
from django.views.generic.edit import DeleteView

from .forms import WorkoutsForm, ExerciseForm
from .models import Workouts, Exercise

# Workouts
class WorkoutsListView(ListView):
    model = Workouts
    context_object_name = 'workouts'

class WorkoutsCreateView(CreateView):
    model = Workouts
    success_url = '/exercise/add'
    form_class = WorkoutsForm
    
class WorkoutsDetailView(DetailView):
    model = Workouts
    context_object_name = 'workout'

    def get_context_data(self, **kwargs: Any):
        context = super().get_context_data(**kwargs)
        context['exercise_list'] = Exercise.objects.all()
        return context

         

# Exercise
class ExerciseListView(ListView):
    model = Exercise
    context_object_name = 'exercise'
    template_name = 'workouts/exercise_list.html'

class ExerciseCreateView(CreateView):
    model = Exercise
    template_name = 'workouts/exercise_form.html'
    form_class = ExerciseForm
    success_url = 'workouts/<int:pk>/'
# Old

# class WorkoutsDeleteView(DeleteView):
#     model = Workouts
#     success_url = '/workouts'
#     template_name = 'workouts/workouts_delete.html'

# class WorkoutsUpdateView(UpdateView):
#     model = Workouts
#     success_url = '/workouts'
#     form_class = WorkoutsForm


    
