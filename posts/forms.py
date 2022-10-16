from .models import Category, Post, Comment
from django.forms import ModelForm, Select, TextInput
from django_summernote.widgets import SummernoteWidget
from crispy_forms.helper import FormHelper

choices = Category.objects.all().values_list('name', 'name')
choice_list = []
for choice in choices:
    choice_list.append(choice)


class PostForm(ModelForm):
    """
    Represent a form for creating a post
    """

    class Meta:
        model = Post
        fields = ('category', 'title', 'body')
        widgets = {
            'category': Select(
                choices=choice_list,
                attrs={
                    'class': 'form-select'}),
            'title': TextInput(),
            'body': SummernoteWidget()}


class CommentForm(ModelForm):
    """
    Represent a form for leaving a comment
    """

    def __init__(self, *args, **kwargs):
        super(CommentForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper(form=self)
        self.fields['body'].label = False

    class Meta:
        model = Comment
        fields = ('body',)
