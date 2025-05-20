from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView, View
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.urls import reverse_lazy
from .models import Service, Booking, Category
from .forms import ServiceForm, BookingForm

class ServiceListView(View):
  def get(self, request):
    services = Service.objects.all().order_by('-created_at')
    categories = Category.objects.all()
    context = {
      'services':services,
      'categories':categories,
    }
    return render(request,'home.html',context)
  # model = Service
  # template_name = 'home.html'
  # context_object_name = 'services'
  # ordering = ['-created_at']
  # pagination = 9
  
  # def get_context_data(self, **kwargs):
  #   context =  super().get_context_data(**kwargs)
  #   context['categories'] = Category.objects.all()
  #   return context

class ServiceDetailView(DetailView):
  model = Service
  template_name = 'service_detail.html'

class ServiceCreateView(LoginRequiredMixin, CreateView):
  model = Service
  form_class = ServiceForm
  template_name = 'service_form.html'
  success_url = reverse_lazy('home')
  
  def form_valid(self, form):
    form.instance.provider = self.request.user
    return super().form_valid(form)
  

class ServiceUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
  model = Service
  form_class = ServiceForm
  template_name = 'service_form.html'
  success_url = reverse_lazy('home')
  
  def test_func(self):
    service = self.get_object()
    return self.request.user == service.provider
  
class ServiceDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
  model = Service
  success_url = reverse_lazy('home')
  template_name = 'service_confirm_delete.html'
  
  def test_func(self):
    service = self.get_object()
    return self.request.user == service.provider


class BookingCreateView(CreateView):
  model = Booking
  template_name = 'booking/booking_form.html'
  form_class = BookingForm
  success_url = reverse_lazy('bookings')
  
  def form_valid(self, form):
    form.instance.client = self.request.user
    form.instance.service = Service.objects.get(pk = self.kwargs['pk'])
    return super().form_valid(form)
  
class BookingListView(ListView):
  model = Booking
  template_name = 'booking/bookings.html'
  context_object_name = 'bookings'
  paginate_by = 10
  
  def get_queryset(self):
    return Booking.objects.filter(client=self.request.user).order_by('-created_at')
  

# my service bookings
class MyServiceBookings(LoginRequiredMixin, ListView):
  model = Booking
  template_name = 'booking/my_service_bookings.html'
  context_object_name = 'bookings'
  
  def get_queryset(self):
    return Booking.objects.filter(service__provider=self.request.user)
  

class BookingStatusUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
  model = Booking
  fields = ['status']
  template_name = 'booking/update_status.html'
  success_url = reverse_lazy('my-service-bookings')
  
  def test_func(self):
    booking = self.get_object()
    return booking.service.provider == self.request.user