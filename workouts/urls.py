from django.urls import path
from . import views

urlpatterns = [
    # Workouts
    path('workouts', views.WorkoutsListView.as_view(), name='workouts_list'),
    path('workouts/add', views.WorkoutsCreateView.as_view(), name='workouts_add'),
    path('workouts/<int:pk>', views.WorkoutsDetailView.as_view(), name='workouts_detail'),
    path('workouts/<int:pk>/edit', views.WorkoutsUpdateView.as_view(), name='workouts_edit'),
    path('workouts/<int:pk>/delete', views.WorkoutsDeleteView.as_view(), name='workouts_delete'),

    # Exerise
    path('workouts/exercise/add/<int:workout_id>/', views.ExerciseCreateView.as_view(), name='exercise_add'),
    path('workouts/exercise/add/<int:pk>/edit', views.ExerciseUpdateView.as_view(), name='exercise_edit'),
    path('workouts/exercise/add/<int:pk>/delete', views.ExerciseDeleteView.as_view(), name='exercise_delete'),
]