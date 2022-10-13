from django.urls import path
from . import views

urlpatterns = [
    path(
        'create_post/',
        views.PostCreateView.as_view(),
        name='create_post'),
    path(
        '<str:category_name>/<int:post_id>/',
        views.PostDetailView.as_view(),
        name='read_post'),
]
