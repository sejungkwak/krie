from django.urls import path
from . import views

urlpatterns = [
    path('<slug:category_slug>/create_post/',
         views.PostCreateView.as_view(),
         name='create_post'),
    path('<slug:category_slug>/<int:post_id>/',
         views.PostDetailView.as_view(),
         name='read_post'),
    path('<slug:category_slug>/<int:pk>/edit_post',
         views.PostUpdateView.as_view(),
         name='update_post'),
    path('<slug:category_slug>/<int:pk>/delete_post/',
         views.PostDeleteView.as_view(),
         name='delete_post'),
    path('<slug:category_slug>/<int:post_id>/edit_comment/<int:pk>/',
         views.CommentUpdateView.as_view(),
         name='update_comment'),
    path('<slug:category_slug>/<int:post_id>/<int:pk>/delete_comment/',
         views.CommentDeleteView.as_view(),
         name='delete_comment'),
    path('<slug:category_slug>/',
         views.PostListView.as_view(),
         name='post_list'),
    path('like/<int:pk>',
         views.PostLikeView.as_view(),
         name='post_like')
]
