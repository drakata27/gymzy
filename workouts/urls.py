from django.urls import path
from . import views

urlpatterns = [
    path('workouts', views.WorkoutsListView.as_view(), name='workouts.list'),
    path('workouts/<int:pk>', views.WorkoutsDetailView.as_view(), name='workouts.detail'),
]