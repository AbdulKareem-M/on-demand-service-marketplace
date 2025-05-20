from django.db import models
from django.contrib.auth.models import User

class Category(models.Model):
  name = models.CharField(max_length=100)
  description = models.TextField(blank=True)
  created_at = models.DateTimeField(auto_now_add=True)
  
  class Meta:
    verbose_name_plural = 'Categories'
    
  def __str__(self) -> str:
    return self.name
  


class Service(models.Model):
  title = models.CharField(max_length=200)
  description = models.TextField()
  price = models.DecimalField(max_digits=10, decimal_places=2)
  category = models.ForeignKey(Category, on_delete=models.CASCADE)
  provider = models.ForeignKey(User, on_delete=models.CASCADE)
  image = models.ImageField(upload_to='services/', blank=True)
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)
  is_available = models.BooleanField(default=True)
  
  def __str__(self):
    return self.title
  

class Booking(models.Model):
  STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('confirmed', 'Confirmed'),
        ('completed', 'Completed'),
        ('cancelled', 'Cancelled'),
    ]
  
  service = models.ForeignKey(Service, on_delete=models.CASCADE)
  client = models.ForeignKey(User, on_delete=models.CASCADE)
  booking_date = models.DateTimeField()
  status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')
  created_at = models.DateTimeField(auto_now_add=True)
  notes = models.TextField(blank=True)
  
  def __str__(self) -> str:
    return f'{self.service.title} - {self.client.username}'
