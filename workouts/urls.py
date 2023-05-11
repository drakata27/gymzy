from django.urls import path
from . import views

urlpatterns = [
    path('workouts', views.WorkoutsListView.as_view(), name='workouts.list'),

    path('workouts/<int:pk>', views.WorkoutsDetailView.as_view(), name='workouts.detail'),
    path('workouts/<int:pk>/edit', views.WorkoutsUpdateView.as_view(), name='workouts.edit'),
    path('workouts/<int:pk>/delete', views.WorkoutsDeleteView.as_view(), name='workouts.delete'),
    path('workouts/add', views.WorkoutsCreateView.as_view(), name='workouts.create'),

    # path('workouts/<int:pk>/details/', views.WorkoutsDetailListView.as_view(), name='workouts.detail-list'),
]