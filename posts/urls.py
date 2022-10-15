from django.urls import path
from . import views

urlpatterns = [
    path(
        'create_post/',
        views.PostCreateView.as_view(),
        name='create_post'),
    path(
        '<slug:category_slug>/<int:post_id>/',
        views.PostDetailView.as_view(),
        name='read_post'),
    path(
        '<slug:category_slug>/<int:pk>/delete_post/',
        views.PostDeleteView.as_view(),
        name='delete_post'),
    path(
        '<slug:category_slug>/',
        views.PostListView.as_view(),
        name='post_list'
    ),
    path(
        'like/<int:pk>',
        views.PostLikeView.as_view(),
        name='post_like'
    ),
]
