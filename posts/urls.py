from django.urls import path
from . import views

urlpatterns = [
    path(
        '<int:category_id>/',
        views.PostListView.as_view(),
        name='post_list'
    ),
    path(
        'create_post/',
        views.PostCreateView.as_view(),
        name='create_post'),
    path(
        '<str:category_name>/<int:post_id>/',
        views.PostDetailView.as_view(),
        name='read_post'),
    path(
        '<str:category_name>/<int:pk>/delete_post/',
        views.PostDeleteView.as_view(),
        name='delete_post'),
]
