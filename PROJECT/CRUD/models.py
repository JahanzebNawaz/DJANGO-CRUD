from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name='User')
    image = models.ImageField(default='img/user.jpg', upload_to='media', verbose_name='Profile Pic')

    class Meta:
        verbose_name_plural = 'User Profile'

    def __str__(self):
        return f'{self.user.username} Profile'
