from typing import Any, Dict
from django.forms.models import BaseModelForm
from django.urls import reverse_lazy
from django.shortcuts import render, redirect
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

    # def get_context_data(self, **kwargs: Any):
    #     context = super().get_context_data(**kwargs)
    #     context['exercise_list'] = Exercise.objects.all()
    #     return context

         

# Exercise
class ExerciseListView(ListView):
    model = Exercise
    context_object_name = 'exercise'
    template_name = 'workouts/exercise_list.html'

class ExerciseCreateView(CreateView):
    model = Exercise
    template_name = 'workouts/exercise_form.html'
    form_class = ExerciseForm
    success_url = '/workouts/detail/'
    
    def form_valid(self, form):
        workout_id = form.instance.workouts.id
        self.object = form.save(commit=False)
        self.object.submitted_by = self.request.user
        self.object.save()
        
        if form.is_valid:
            form.save()
        return redirect(reverse_lazy('workouts_detail', args=[workout_id]))
    
    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['initial'] = {'workouts': self.kwargs['workout_id']}
        return kwargs
    
    def get_success_url(self):
        return '/workouts/{}/'.format(self.kwargs['workout_id'])
        
    
    
# Old

# class WorkoutsDeleteView(DeleteView):
#     model = Workouts
#     success_url = '/workouts'
#     template_name = 'workouts/workouts_delete.html'

# class WorkoutsUpdateView(UpdateView):
#     model = Workouts
#     success_url = '/workouts'
#     form_class = WorkoutsForm


    
