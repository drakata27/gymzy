from django.urls import reverse_lazy
from django.shortcuts import redirect
from django.views.generic import CreateView,DetailView, ListView, UpdateView
from django.views.generic.edit import DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http.response import HttpResponseRedirect

from .forms import WorkoutsForm, ExerciseForm
from .models import Workouts, Exercise

# Workouts
class WorkoutsDeleteView(LoginRequiredMixin,DeleteView):
    model = Workouts
    template_name = 'workouts/workouts_delete.html'
    success_url = '/workouts'
    login_url = '/admin'
    

class WorkoutsCreateView(LoginRequiredMixin, CreateView):
    model = Workouts
    form_class = WorkoutsForm
    login_url = '/admin'

    def get_success_url(self):
        return reverse_lazy('workouts_detail', args=[self.object.pk])
    
    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.save()
        return HttpResponseRedirect(self.get_success_url())

class WorkoutsUpdateView(LoginRequiredMixin, UpdateView):
    model = Workouts
    form_class = WorkoutsForm
    login_url = '/admin'

    def get_success_url(self):
        return reverse_lazy('workouts_detail', args=[self.object.pk])

class WorkoutsListView(LoginRequiredMixin, ListView):
    model = Workouts
    context_object_name = 'workouts'
    login_url = '/admin'

    def get_queryset(self):
        return self.request.user.workouts.all()
    
class WorkoutsDetailView(LoginRequiredMixin, DetailView):
    model = Workouts
    context_object_name = 'workout'
    login_url = '/admin'

# Exercise
class ExerciseDeleteView(DeleteView):
    model = Exercise
    template_name = 'workouts/exercise_delete.html'

    def get_success_url(self):
        workout_id = self.object.workouts.id
        return reverse_lazy('workouts_detail', kwargs={'pk': workout_id})
    

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
    
class ExerciseUpdateView(UpdateView):
    model = Exercise
    form_class = ExerciseForm
    
    # Check
    def form_valid(self, form):
        workout_id = form.instance.workouts.id
        self.object = form.save(commit=False)
        self.object.submitted_by = self.request.user
        self.object.save()
        
        if form.is_valid:
            form.save()
        return redirect(reverse_lazy('workouts_detail', args=[workout_id]))


    
