from django.contrib import admin
from .models import Category, Post, Comment
from django_summernote.admin import SummernoteModelAdmin


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    """
    Category panel for the admin site
    """
    list_display = ('name',)
    search_fields = ['name']


@admin.register(Post)
class PostAdmin(SummernoteModelAdmin):
    """
    Post panel for the admin site
    """
    list_display = (
        'id',
        'category',
        'title',
        'author',
        'created_on',
        'updated_on')
    search_fields = ['author', 'title']
    summernote_fields = ('body',)
    actions = ['delete_selected']


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    """
    Comment panel for the admin site
    """
    list_display = (
        'original_post',
        'body',
        'author',
        'created_on',
        'updated_on')
    search_fields = ['author']
    actions = ['delete_selected']
