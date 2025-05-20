from django import forms
from .models import Service, Booking

class ServiceForm(forms.ModelForm):
  class Meta:
    model = Service
    fields = ['title', 'description', 'price', 'category', 'image', 'is_available']
    widgets = {
      'description': forms.Textarea(attrs={'rows': 4})
    }
    
class BookingForm(forms.ModelForm):
  class Meta:
    model = Booking
    fields = ['booking_date', 'notes']
    widgets = {
      'booking_date': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
      'notes': forms.Textarea(attrs={'rows': 3})
    }    
