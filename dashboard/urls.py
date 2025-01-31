from . import views
from django.urls import path, include

urlpatterns = [
    path('', views.resident_dashboard, name='dashboard'),
    path(
        'edit_booking/<int:booking_id>',
        views.booking_edit,
        name='booking_edit'
        ),
    path('event_space_booking/', views.event_space_booking, name='booking'),
    path('event_spaces/', views.event_spaces_list, name='event_spaces'),
    path(
        'event_space_booking/<int:space_id>',
        views.event_space_booking,
        name='space_booking'
        ),
    path(
        'delete_booking/<int:booking_id>',
        views.booking_delete,
        name='booking_delete'
        ),
    path('submit_request/', views.submit_request, name='resident_request'),
]
