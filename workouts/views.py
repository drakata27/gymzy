from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render
from django.views.generic import CreateView,DetailView, ListView, UpdateView
from django.views.generic.edit import DeleteView

from .forms import WorkoutsForm, ExerciseForm
from .models import Workouts, Exercise

# List
class WorkoutsListView(ListView):
    model = Workouts
    context_object_name = 'workouts'

class WorkoutsCreateView(CreateView):
    model = Workouts
    success_url = '/exercise/add'
    form_class = WorkoutsForm

class ExerciseListView(ListView):
    model = Exercise
    context_object_name = 'exercise'
    template_name = 'workouts/exercise_list.html'

class ExerciseCreateView(CreateView):
    model = Exercise
    template_name = 'workouts/exercise_form.html'
    success_url = '/exercise'
    form_class = ExerciseForm
# Old

# class WorkoutsDeleteView(DeleteView):
#     model = Workouts
#     success_url = '/workouts'
#     template_name = 'workouts/workouts_delete.html'

# class WorkoutsUpdateView(UpdateView):
#     model = Workouts
#     success_url = '/workouts'
#     form_class = WorkoutsForm


    
# class WorkoutsDetailView(DetailView):
#     model = Workouts
#     context_object_name = 'workout'