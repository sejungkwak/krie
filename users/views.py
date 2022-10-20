from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.list import ListView
from .models import Profile
from posts.models import Post, Comment


class ProfileDetailView(LoginRequiredMixin, ListView):
    """
    Profile view for users to view their own profile and others
    """

    model = Profile
    template_name = 'users/read_profile.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['profile'] = Profile.objects.get(pk=self.kwargs['pk'])
        context['posts'] = Post.objects.filter(
            author=self.kwargs['pk']).order_by('-created_on')
        context['comments'] = Comment.objects.filter(
            author=self.kwargs['pk']).order_by('-created_on')
        return context
