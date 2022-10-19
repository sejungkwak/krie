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
    model = Post
    template_name = 'posts/post_list.html'
    paginate_by = 10

    def get_queryset(self):
        return super().get_queryset().filter(
            category__slug=self.kwargs['category_slug'])

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['posts'] = Post.objects.filter(
            category__slug=self.kwargs['category_slug'])
        return context


class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    template_name = 'posts/create_post.html'
    form_class = PostForm

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy(
            'read_post', kwargs={
                'category_slug': self.object.category.slug,
                'post_id': self.object.id})


class PostDetailView(View):

    template_name = 'posts/read_post.html'

    def get(self, request, *arg, **kwargs):
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

    model = Post
    template_name = 'posts/create_post.html'
    form_class = PostForm

    def test_func(self):
        if self.get_object().author == self.request.user:
            return True

    def get_success_url(self):
        return reverse_lazy(
            'read_post', kwargs={
                'category_slug': self.object.category.slug, 'post_id': self.object.id})


class PostDeleteView(UserPassesTestMixin, DeleteView):

    model = Post
    template_name = 'posts/delete_post.html'

    def test_func(self):
        if self.get_object().author == self.request.user:
            return True

    def delete(self, request, *args, **kwargs):
        object = self.get_object()
        return super().delete(request, *args, **kwargs)

    def get_success_url(self):
        return reverse_lazy(
            'post_list', kwargs={
                'category_slug': self.object.category.slug})


class CommentUpdateView(UserPassesTestMixin, UpdateView):

    model = Comment
    form_class = CommentForm
    template_name = 'posts/read_post.html'

    def test_func(self):
        if self.get_object().author == self.request.user:
            return True

    def get(self, request, *arg, **kwargs):
        id = self.kwargs.get('post_id')
        post = get_object_or_404(Post, pk=id)
        comments = post.comments.all().exclude(pk=self.kwargs.get('pk')).order_by('-created_on')
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
        return reverse_lazy('read_post', kwargs={
                'category_slug': self.object.original_post.category.slug,
                'post_id': self.object.original_post.id})


class CommentDeleteView(UserPassesTestMixin, DeleteView):

    model = Comment
    template_name = 'posts/delete_comment.html'

    def test_func(self):
        if self.get_object().author == self.request.user:
            return True

    def delete(self, request, *args, **kwargs):
        object = self.get_object()
        return super().delete(request, *args, **kwargs)

    def get_success_url(self):
        return reverse_lazy(
            'read_post', kwargs={
                'category_slug': self.object.original_post.category.slug,
                'post_id': self.object.original_post.id})


class PostLikeView(View):

    def post(self, request, *arg, **kwargs):
        post = get_object_or_404(Post, id=request.POST.get('post_id'))

        if post.likes.filter(id=request.user.id).exists():
            post.likes.remove(request.user)
        else:
            post.likes.add(request.user)

        return HttpResponseRedirect(self.request.META.get('HTTP_REFERER'))
