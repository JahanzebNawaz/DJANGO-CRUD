from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name='User')
    image = models.ImageField(default='img/user.jpg', upload_to='images', verbose_name='Profile Pic')

    class Meta:
        verbose_name_plural = 'User Profile'

    def __str__(self):
        return f'{self.user.username} Profile'
    
    def save(self):
        super().save()

        img = Image.open(self.image.path)

        if img.height > 300 or img.width > 300:
            outpust_size = (300, 300)
            img.thumbnail(outpust_size)
            img.save(self.image.path)


class Courses(models.Model):
    course_name = models.CharField(max_length=30, verbose_name='Course Name')
    course_duration = models.CharField(max_length=30, verbose_name='Course Duration')
    course_amount = models.IntegerField(verbose_name='Course Amount')
    course_details = models.TextField(max_length=1000, verbose_name='Course Details')
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Author')
    
    created_on = models.DateTimeField(auto_now_add = True)
    updated_on = models.DateTimeField(auto_now = True)
    image = models.FileField(upload_to='course')

    class Meta:
        ordering = ['-created_on']
        verbose_name_plural  = 'Courses'

    def date_pretty(self):
        return self.created_on.strftime('%b %e, %Y')

    def summary(self):
        return self.course_details[:30]

    def __str__(self):
        return self.course_name

    
    