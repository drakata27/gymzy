from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render
from django.views.generic import CreateView,DetailView, ListView, UpdateView
from django.views.generic.edit import DeleteView

from .forms import WorkoutsForm
from .models import Workouts

# Create your views here.
# class WorkoutsDetailListView(ListView):
#     model = Workouts
#     context_object_name = 'workoutdetails'
#     template_name = 'workouts/workouts_detail_list.html'

class WorkoutsDeleteView(DeleteView):
    model = Workouts
    success_url = '/workouts'
    template_name = 'workouts/workouts_delete.html'

class WorkoutsUpdateView(UpdateView):
    model = Workouts
    success_url = '/workouts'
    form_class = WorkoutsForm

class WorkoutsCreateView(CreateView):
    model = Workouts
    success_url = '/workouts'
    form_class = WorkoutsForm

class WorkoutsListView(ListView):
    model = Workouts
    context_object_name = 'workouts'
    # template_name = 'workouts/workouts_list.html'

    # def get_queryset(self):
    #     return self.request.user.workouts.all()
    
class WorkoutsDetailView(DetailView):
    model = Workouts
    context_object_name = 'workout'