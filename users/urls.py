from django.urls import path
from . import views

urlpatterns = [
    path('profile/<int:pk>/',
         views.ProfileDetailView.as_view(),
         name='read_profile'),
    path('profile/<int:pk>/edit/',
         views.ProfileUpdateView.as_view(),
         name='update_profile')
]
