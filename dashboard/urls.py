from . import views
from django.urls import path, include

urlpatterns = [
    path('', views.resident_dashboard, name='dashboard'),
    path('event_space_booking/', views.event_space_booking, name='booking'),
]
