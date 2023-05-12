from django.urls import path
from . import views

urlpatterns = [
    path('workouts', views.WorkoutsListView.as_view(), name='workouts_list'),
    path('workouts/add', views.WorkoutsCreateView.as_view(), name='workouts_add'),
    path('workouts/<int:pk>', views.WorkoutsDetailView.as_view(), name='workouts_detail'),

    # path('workouts/<int:pk>', views.ExerciseListView.as_view(), name='exercise_list'),
    path('workouts/exercise/add/<int:workout_id>/', views.ExerciseCreateView.as_view(), name='exercise_add'),

    # path('workouts/<int:pk>/edit', views.WorkoutsUpdateView.as_view(), name='workouts.edit'),
    # path('workouts/<int:pk>/delete', views.WorkoutsDeleteView.as_view(), name='workouts.delete'),

]