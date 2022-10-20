from django.urls import path
from . import views

urlpatterns = [
    path('', views.get_home, name='home'),
    path('search_results/', views.SearchView.as_view(), name='search_results')
]
