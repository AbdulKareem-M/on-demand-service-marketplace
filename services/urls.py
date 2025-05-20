from django.urls import path
from .views import (
    ServiceListView,
    ServiceDetailView,
    ServiceCreateView,
    ServiceUpdateView,
    ServiceDeleteView,
    BookingCreateView,
    BookingListView,
    MyServiceBookings,
    BookingStatusUpdateView,
)

urlpatterns = [
    path('', ServiceListView.as_view(), name='home'),
    path('service/<int:pk>/', ServiceDetailView.as_view(), name='service-detail'),
    path('service/new/', ServiceCreateView.as_view(), name='service-create'),
    path('service/<int:pk>/update/', ServiceUpdateView.as_view(), name='service-update'),
    path('service/<int:pk>/delete/', ServiceDeleteView.as_view(), name='service-delete'),
    path('service/<int:pk>/book/', BookingCreateView.as_view(), name='booking-create'),
    path('bookings/', BookingListView.as_view(), name='bookings'),
    path('my-bookings/', MyServiceBookings.as_view(), name='my-service-bookings'),
    path('booking/<int:pk>/update/', BookingStatusUpdateView.as_view(), name='booking-update'),

]