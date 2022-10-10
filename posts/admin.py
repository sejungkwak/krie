from django.contrib import admin
from .models import Category, Post, Comment


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    """
    Category panel for the admin site
    """
    list_display = ('name',)
    search_fields = ['name']


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    """
    Post panel for the admin site
    """
    list_display = (
        'category',
        'title',
        'author',
        'created_on',
        'updated_on')
    search_fields = ['author', 'title']
    actions = ['delete_selected']


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    """
    Comment panel for the admin site
    """
    list_display = (
        'original_post',
        'author',
        'created_on',
        'updated_on')
    search_fields = ['author']
    actions = ['delete_selected']
