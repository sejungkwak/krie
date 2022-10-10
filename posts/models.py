from django.db import models
from django.contrib.auth.models import User


class Category(models.Model):
    """
    Category database model
    """
    name = models.CharField(max_length=15, unique=True)

    def __str__(self):
        return self.name


class Post(models.Model):
    """
    Post database model
    """
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='posts')
    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        related_name='posts')
    title = models.CharField(max_length=30)
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    likes = models.ManyToManyField(User, related_name='post_likes', blank=True)

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return self.title

    def number_of_likes(self):
        return self.likes.count()


class Comment(models.Model):
    """
    Comment database model
    """
    original_post = models.ForeignKey(
        Post, on_delete=models.CASCADE, related_name='comments')
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='comments')
    body = models.CharField(max_length=255)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return self.body
