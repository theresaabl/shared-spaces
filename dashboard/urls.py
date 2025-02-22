from . import views
from django.urls import path
from .views import MyCustomLoginView

urlpatterns = [
    # general dashboard urls
    path('', views.resident_dashboard, name='dashboard'),

    # custom login view
    path("accounts/login/", MyCustomLoginView.as_view(), name="account_login"),

    # edit bookings
    path(
        'edit_booking/<int:booking_id>',
        views.booking_edit,
        name='booking_edit'
        ),
    # edit resident requests
    path(
        'edit_resident_request/<int:resident_request_id>',
        views.resident_request_edit,
        name='resident_request_edit'
        ),
    # event space booking
    path('event_space_booking/', views.event_space_booking, name='booking'),
    # event spaces list
    path('event_spaces/', views.event_spaces_list, name='event_spaces'),
    # event space booking for a specific event space
    path(
        'event_space_booking/<int:space_id>',
        views.event_space_booking,
        name='space_booking'
        ),
    # delete event space booking
    path(
        'delete_booking/<int:booking_id>',
        views.booking_delete,
        name='booking_delete'
        ),
    # delete resident request
    path(
        'delete_resident_request/<int:resident_request_id>',
        views.resident_request_delete,
        name='resident_request_delete'
        ),
    # submit resident request
    path('submit_request/', views.submit_request, name='resident_request'),
]
