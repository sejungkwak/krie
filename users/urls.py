from django.urls import path
from . import views

urlpatterns = [
    path('profile/<int:pk>/activity/posts/',
         views.ProfilePostListView.as_view(),
         name='read_profile_posts'),
    path('profile/<int:pk>/activity/comments/',
         views.ProfileCommentListView.as_view(),
         name='read_profile_comments'),
    path('profile/<int:pk>/about/',
         views.ProfileAboutView.as_view(),
         name='read_profile_about'),
    path('profile/<int:pk>/edit/',
         views.ProfileUpdateView.as_view(),
         name='update_profile')
]
