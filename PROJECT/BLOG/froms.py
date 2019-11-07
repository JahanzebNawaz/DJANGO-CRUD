from django import forms
from .models import BlogPost


class BlogPostForm(forms.ModelForm):
    class Meta:
        model = BlogPost
        fields = ['blog_title', 'blog_heading', 'blog_details', 'author', 'image']



class BlogUpdateForm(forms.ModelForm):
    class Meta:
        model = BlogPost
        fields = ['blog_title', 'blog_heading', 'blog_details', 'author', 'image']

        