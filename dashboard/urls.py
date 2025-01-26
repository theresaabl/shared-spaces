from . import views
from django.urls import path, include

urlpatterns = [
    path('', views.resident_dashboard, name='dashboard'),
    path('event_space_booking/', views.event_space_booking, name='booking'),
    path('edit_booking/<int:booking_id>', views.booking_edit, name='booking_edit'),
    path('delete_booking/<int:booking_id>', views.booking_delete, name='booking_delete'),
]
