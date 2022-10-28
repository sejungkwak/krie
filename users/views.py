from django.shortcuts import render, get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.views.generic import UpdateView
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from posts.models import Post, Comment
from .models import Profile
from .forms import UserUpdateForm, ProfileUpdateForm


class ProfileAboutView(LoginRequiredMixin, DetailView):
    """
    Display a user's location and bio.
    """
    model = Profile
    template_name = 'users/read_profile.html'

    def get_context_data(self, **kwargs):
        """
        Retrieve the specified user's profile data.
        """
        context = super().get_context_data(**kwargs)
        context['profile'] = Profile.objects.get(pk=self.kwargs['pk'])
        return context


class ProfilePostListView(LoginRequiredMixin, ListView):
    """
    Display a list of posts written by the specified user.
    """
    model = Post
    template_name = 'users/read_profile_posts.html'
    paginate_by = 10

    def get_queryset(self):
        """
        Get a user to display.
        """
        return super().get_queryset().filter(author=self.kwargs['pk'])

    def get_context_data(self, **kwargs):
        """
        Retrieve a list of posts written by the specified user.
        """
        context = super().get_context_data(**kwargs)
        context['profile'] = Profile.objects.get(pk=self.kwargs['pk'])
        context['posts'] = Post.objects.filter(
            author=self.kwargs['pk']).order_by('-created_on')
        return context


class ProfileCommentListView(LoginRequiredMixin, ListView):
    """
    Display a list of comments written by the specified user.
    """
    model = Comment
    template_name = 'users/read_profile_comments.html'
    paginate_by = 6

    def get_queryset(self):
        """
        Get a user to display.
        """
        return super().get_queryset().filter(author=self.kwargs['pk'])

    def get_context_data(self, **kwargs):
        """
        Retrieve a list of comments written by the specified user.
        """
        context = super().get_context_data(**kwargs)
        context['profile'] = Profile.objects.get(pk=self.kwargs['pk'])
        context['comments'] = Comment.objects.filter(
            author=self.kwargs['pk']).order_by('-created_on')
        return context


class ProfileUpdateView(UserPassesTestMixin, SuccessMessageMixin, UpdateView):
    """
    Edit a user's own profile.
    """
    model = Profile
    user_form_class = UserUpdateForm
    profile_form_class = ProfileUpdateForm
    template_name = 'users/update_profile.html'
    success_message = 'Your profile has been successfully updated.'

    def test_func(self):
        """
        Check if the logged-in user is the owner of the account.
        """
        if self.get_object().id == self.request.user.pk:
            return True

    def get(self, request, *args, **kwargs):
        """
        Retrieve the user's profile data and display current values in the form.
        """
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
        """
        Update the user's profile data.
        """
        user_form = self.user_form_class(
            data=request.POST, instance=request.user)
        profile_form = self.profile_form_class(
            data=request.POST, instance=request.user.profile)

        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(
                request, 'Your profile has been successfully updated.')
        else:
            get_error_text = user_form.errors.as_text().split('*')[-1]
            messages.error(request, get_error_text)
        return HttpResponseRedirect(self.get_success_url())

    def get_success_url(self):
        """
        Redirect back to the same page and display the updated data.
        """
        return reverse_lazy(
            'update_profile', kwargs={
                'pk': self.request.user.pk})
