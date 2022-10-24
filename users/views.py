from django.shortcuts import render, get_object_or_404
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.views.generic import UpdateView
from django.views.generic.list import ListView
from posts.models import Post, Comment
from .models import Profile
from .forms import UserUpdateForm, ProfileUpdateForm


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


class ProfileUpdateView(UserPassesTestMixin, UpdateView):
    """
    Profile update view for users to edit their own profile
    """

    model = Profile
    user_form_class = UserUpdateForm
    profile_form_class = ProfileUpdateForm
    template_name = 'users/update_profile.html'

    def test_func(self):
        if self.get_object().id == self.request.user.pk:
            return True

    def get(self, request, *args, **kwargs):
        id = self.kwargs.get('pk')
        profile = get_object_or_404(Profile, pk=id)
        username = profile.user.username
        email = profile.user.email
        location = profile.location
        bio = profile.bio
        user_form = self.user_form_class
        profile_form = self.profile_form_class
        return render(request, self.template_name, {
            'user_form': user_form(initial={'username': username, 'email': email}),
            'profile_form': profile_form(initial={'location': location, 'bio': bio})
        })

    def post(self, request, *args, **kwargs):
        user_form = self.user_form_class(data=request.POST, instance=request.user)
        profile_form = self.profile_form_class(data=request.POST, instance=request.user.profile)

        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.add_message(request, messages.SUCCESS, 'Your profile has been updated successfully.')
            return HttpResponseRedirect(self.get_success_url())
        else:
            messages.add_message(request, messages.ERROR, 'That username is already in use.')
        return HttpResponseRedirect(self.get_success_url())

    def get_success_url(self):
        return reverse_lazy('update_profile', kwargs={'pk': self.request.user.pk})
