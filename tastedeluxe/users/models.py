from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    delivery_adress = models.CharField(max_length=100, blank=True)
    pay_card = models.CharField(max_length=16, blank=True)

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')

    def __str__(self):
        return f'{self.user.username} Profile'