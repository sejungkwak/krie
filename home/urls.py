from django.urls import path
from django.views.generic import TemplateView
from . import views

urlpatterns = [
    path('',
         TemplateView.as_view(
             template_name='home/index.html'),
         name='home'),
    path('search_results/',
         views.SearchView.as_view(),
         name='search_results'),
    path('privacy_policy/',
         TemplateView.as_view(
             template_name='home/privacy_policy.html'),
         name='privacy_policy'),
    path('terms_and_conditions/',
         TemplateView.as_view(
             template_name='home/terms_conditions.html'),
         name='terms_conditions')]
