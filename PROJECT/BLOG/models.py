from django.db import models
from django.conf import settings
from django.contrib.auth.models import User

# Create your models here.


class BlogPost(models.Model):
    blog_title = models.CharField(max_length=100, verbose_name='Blog Title')
    blog_heading = models.CharField(max_length=100, verbose_name='Blog Heading')
    blog_details = models.TextField(verbose_name='Blog Details')

    author = models.ForeignKey(settings.AUTH_USER_MODEL, default=1, on_delete=models.CASCADE, related_name='blog_posts')
    created_on = models.DateTimeField(auto_now_add = True)
    updated_on = models.DateTimeField(auto_now = True)
    image = models.ImageField(upload_to = 'blog/images', default='')

    
    class Meta:
        ordering = ['-created_on']
        verbose_name_plural = 'Blogs'

    
    def date_pretty(self):
        return self.created_on.strftime('%b %e, %Y')

    def summary_title(self):
        return self.blog_title[:30]

    def summary(self):
        return self.blog_details[:50]
    
    
    def __str__(self):
        return '%s ' %(self.blog_title )