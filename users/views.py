from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import DetailView
from .models import Profile
from posts.models import Post, Comment


class ProfileDetailView(LoginRequiredMixin, DetailView):
    """
    Profile view for users to view their own profile and others
    """

    model = Profile
    template_name = 'users/read_profile.html'

    def get(self, request, pk, *args, **kwargs):
        profile = Profile.objects.get(pk=pk)
        user = profile.user
        posts = Post.objects.filter(author=user).order_by('-created_on')
        comments = Comment.objects.filter(author=user).order_by('-created_on')

        context = {
            'user': user,
            'profile': profile,
            'posts': posts,
            'comments': comments
        }
        return render(request, 'users/read_profile.html', context)
