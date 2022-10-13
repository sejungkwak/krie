from django.shortcuts import render, get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import View
from django.views.generic.edit import CreateView
from .models import Category, Post, Comment
from .forms import PostForm, CommentForm


class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    template_name = 'posts/create_post.html'
    fields = ['category', 'title', 'body']


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
