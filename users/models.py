from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
  user = models.OneToOneField(User, on_delete=models.CASCADE)
  bio = models.TextField(max_length=500, blank=True)
  phone = models.CharField(max_length=10, blank=True)
  address = models.TextField(blank=True)
  image = models.ImageField(upload_to='profile_pics',blank=True)
  
  def __str__(self):
    return f'{self.user.username} Profile'