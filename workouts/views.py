from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render
from django.views.generic import CreateView,DetailView, ListView, UpdateView

from .models import Workouts

# Create your views here.
class WorkoutsListView(ListView):
    model = Workouts
    context_object_name = 'workouts'
    # template_name = 'workouts/workouts_list.html'

    # def get_queryset(self):
    #     return self.request.user.workouts.all()
    
class WorkoutsDetailView(DetailView):
    model = Workouts
    context_object_name = 'workout'
