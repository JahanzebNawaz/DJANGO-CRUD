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

