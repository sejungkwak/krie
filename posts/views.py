from django.shortcuts import render, get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.http import HttpResponseRedirect
from django.urls import reverse, reverse_lazy
from django.views import View
from django.views.generic import UpdateView
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, DeleteView
from .models import Category, Post, Comment
from .forms import PostForm, CommentForm


class PostListView(ListView):
    """
    Display a list of posts per requested category.
    """
    model = Post
    template_name = 'posts/post_list.html'
    paginate_by = 10

    def get_queryset(self):
        """
        Get the requested category.
        """
        return super().get_queryset().filter(
            category__slug=self.kwargs['category_slug'])

    def get_context_data(self, **kwargs):
        """
        Filter posts that are under a specific category.
        """
        context = super().get_context_data(**kwargs)
        context['posts'] = Post.objects.filter(
            category__slug=self.kwargs['category_slug'])
        return context


class PostCreateView(LoginRequiredMixin, CreateView):
    """
    Create a post.
    """
    model = Post
    template_name = 'posts/create_post.html'
    form_class = PostForm

    def get_initial(self, **kwargs):
        """
        Preselect the category value in the form based on the URL path.
        """
        initial = super().get_initial(**kwargs)
        category_name = self.request.path.split('/')[2]
        if category_name == 'rooms':
            category = 1
        elif category_name == 'jobs':
            category = 2
        elif category_name == 'visas':
            category = 3
        elif category_name == 'market':
            category = 4
        elif category_name == 'random':
            category = 5
        initial['category'] = category
        return initial

    def form_valid(self, form):
        """
        Save the form with the value of the logged-in user.
        """
        form.instance.author = self.request.user
        return super().form_valid(form)

    def get_success_url(self):
        """
        Render the post detail page after creating it.
        """
        return reverse_lazy(
            'read_post', kwargs={
                'category_slug': self.object.category.slug,
                'post_id': self.object.id})


class PostDetailView(View):
    """
    Display a post detail and handle the post request of a comment.
    """
    template_name = 'posts/read_post.html'

    def get(self, request, *arg, **kwargs):
        """
        Retrieve an individual post, its likes and comments.
        """
        id = self.kwargs.get('post_id')
        post = get_object_or_404(Post, pk=id)
        comments = post.comments.order_by('created_on')
        liked = False
        if post.likes.filter(id=self.request.user.id).exists():
            liked = True
        new_comment = True

        return render(
            request,
            self.template_name,
            {
                'post': post,
                'comments': comments,
                'liked': liked,
                'new_comment': new_comment,
                'comment_form': CommentForm()
            }
        )

    def post(self, request, *arg, **kwargs):
        """
        Save the comment and redirect back to the same page.
        """
        id = self.kwargs.get('post_id')
        post = get_object_or_404(Post, pk=id)
        comment_form = CommentForm(data=request.POST)

        if comment_form.is_valid():
            comment_form.instance.author = request.user
            comment = comment_form.save(commit=False)
            comment.original_post = post
            comment.save()
        else:
            comment_form = CommentForm()

        return HttpResponseRedirect(self.request.META.get('HTTP_REFERER'))


class PostUpdateView(UserPassesTestMixin, UpdateView):
    """
    Edit a post.
    """
    model = Post
    template_name = 'posts/create_post.html'
    form_class = PostForm

    def test_func(self):
        """
        Check if the logged-in user is the owner of the post.
        """
        if self.get_object().author == self.request.user:
            return True

    def get_success_url(self):
        """
        Render the updated post detail page.
        """
        return reverse_lazy(
            'read_post', kwargs={
                'category_slug': self.object.category.slug,
                'post_id': self.object.id})


class PostDeleteView(UserPassesTestMixin, DeleteView):
    """
    Delete an individual post.
    """
    model = Post
    template_name = 'posts/delete_post.html'

    def test_func(self):
        """
        Check if the logged-in user is the owner of the post.
        """
        if self.get_object().author == self.request.user:
            return True

    def delete(self, request, *args, **kwargs):
        """
        Delete the requested post from the database.
        """
        object = self.get_object()
        return super().delete(request, *args, **kwargs)

    def get_success_url(self):
        """
        Render the category list page where the deleted post was.
        """
        return reverse_lazy(
            'post_list', kwargs={
                'category_slug': self.object.category.slug})


class CommentUpdateView(UserPassesTestMixin, UpdateView):
    """
    Edit a comment.
    """
    model = Comment
    form_class = CommentForm
    template_name = 'posts/read_post.html'

    def test_func(self):
        """
        Check if the logged-in user is the owner of the comment.
        """
        if self.get_object().author == self.request.user:
            return True

    def get(self, request, *arg, **kwargs):
        """
        Retrieve the post that the comment belongs.
        """
        id = self.kwargs.get('post_id')
        post = get_object_or_404(Post, pk=id)
        comments = post.comments.all().exclude(
            pk=self.kwargs.get('pk')).order_by('-created_on')
        comment = post.comments.filter(pk=self.kwargs.get('pk')).first()
        liked = False
        if post.likes.filter(id=self.request.user.id).exists():
            liked = True
        new_comment = False

        return render(
            request,
            self.template_name,
            {
                'post': post,
                'comments': comments,
                'liked': liked,
                'new_comment': new_comment,
                'comment_form': CommentForm(instance=comment)
            }
        )

    def get_success_url(self):
        """
        Render the post detail page after saving the edited comment.
        """
        return reverse_lazy('read_post', kwargs={
            'category_slug': self.object.original_post.category.slug,
            'post_id': self.object.original_post.id})


class CommentDeleteView(UserPassesTestMixin, DeleteView):
    """
    Delete an individual comment.
    """
    model = Comment
    template_name = 'posts/delete_comment.html'

    def test_func(self):
        """
        Check if the logged-in user is the owner of the comment.
        """
        if self.get_object().author == self.request.user:
            return True

    def delete(self, request, *args, **kwargs):
        """
        Delete a comment from the database.
        """
        object = self.get_object()
        return super().delete(request, *args, **kwargs)

    def get_success_url(self):
        """
        Render the post detail page after deleting the comment.
        """
        return reverse_lazy(
            'read_post', kwargs={
                'category_slug': self.object.original_post.category.slug,
                'post_id': self.object.original_post.id})


class PostLikeView(View):
    """
    Display the user's interaction with the like button.
    """
    def post(self, request, *arg, **kwargs):
        """
        Toggle the status of a like.
        """
        post = get_object_or_404(Post, id=request.POST.get('post_id'))

        if post.likes.filter(id=request.user.id).exists():
            post.likes.remove(request.user)
        else:
            post.likes.add(request.user)

        return HttpResponseRedirect(self.request.META.get('HTTP_REFERER'))
