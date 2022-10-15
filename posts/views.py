from django.shortcuts import render, get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.http import HttpResponseRedirect
from django.urls import reverse, reverse_lazy
from django.views import View
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, DeleteView
from .models import Category, Post, Comment
from .forms import PostForm, CommentForm


class PostListView(ListView):
    model = Post
    template_name = 'post_list'
    paginated_by = 10

    def get_queryset(self):
        return super().get_queryset().filter(category__slug=self.kwargs['category_slug'])

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['posts'] = Post.objects.filter(category__slug=self.kwargs['category_slug'])
        return context


class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    template_name = 'posts/create_post.html'
    form_class = PostForm
    success_url = reverse_lazy('home')  # temporary redirect url

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class PostDetailView(View):

    template_name = 'posts/read_post.html'

    def get(self, request, *arg, **kwargs):
        queryset = Post.objects.all()
        id = self.kwargs.get('post_id')
        post = get_object_or_404(queryset, pk=id)
        comments = post.comments.order_by('-created_on')
        liked = False
        if post.likes.filter(id=self.request.user.id).exists():
            liked = True

        return render(
            request,
            self.template_name,
            {
                'post': post,
                'comments': comments,
                'commented': False,
                'liked': liked,
                'comment_form': CommentForm()
            }
        )


class PostDeleteView(UserPassesTestMixin, DeleteView):

    model = Post
    template_name = 'posts/delete_post.html'
    success_url = reverse_lazy('home')  # temporary redirect url

    def test_func(self):
        if self.get_object().author == self.request.user:
            return True

    def delete(self, request, *args, **kwargs):
        object = self.get_object()
        return super().delete(request, *args, **kwargs)


class PostLikeView(View):

    def post(self, request, *arg, **kwargs):
        post = get_object_or_404(Post, id=request.POST.get('post_id'))

        if post.likes.filter(id=request.user.id).exists():
            post.likes.remove(request.user)
        else:
            post.likes.add(request.user)

        return HttpResponseRedirect(self.request.META.get('HTTP_REFERER'))
