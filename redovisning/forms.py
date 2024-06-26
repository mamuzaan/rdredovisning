from .models import Comment, Post
from django import forms
from django_summernote.widgets import SummernoteInplaceWidget, SummernoteWidget


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('body',)


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = '__all__'
        widgets = {
            'content': SummernoteWidget(),
        }


class EditForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = '__all__'
        widgets = {
            'content': SummernoteWidget(),
        }


class ContactusForm(forms.Form):
    name = forms.CharField(label='Name', max_length=100, required=True)
    email = forms.EmailField(label='Email', max_length=100, required=True)
    message = forms.CharField(label='Message', widget=forms.Textarea, required=True)
