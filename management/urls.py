from . import views
from django.urls import path

urlpatterns = [
    # Main management page
    path('', views.management_page, name='management'),

    # Event spaces list
    path('event-spaces/', views.event_spaces, name='mgmt-event-spaces'),
    # Add new event space
    path('event-spaces/add-event-space', views.add_event_space, name='mgmt-add-event-space'),
    # Edit existing event space
    path('event-spaces/edit-event-space/<int:space_id>', views.event_space_edit, name='mgmt-edit-event-space'),
    # Delete existing event space
    path('event-spaces/delete-event-space/<int:space_id>', views.event_space_delete, name='mgmt-delete-event-space'),

    # Event space bookings list
    path('event-space-bookings/', views.event_space_bookings, name='mgmt-event-space-bookings'),
    # Approve a booking
    path('event-space-bookings/approve-booking/<int:booking_id>', views.approve_booking, name='mgmt-booking-approve'),
    # Deny a booking
    path('event-space-bookings/deny-booking/<int:booking_id>', views.deny_booking, name='mgmt-booking-deny'),
    # Delete a booking
    path(
        'event-space-bookings/delete-booking/<int:booking_id>',
        views.booking_delete,
        name='mgmt-booking-delete'
        ),

    # Contact messages list
    path('contact-messages/', views.contact_messages, name='mgmt-contact-messages'),
    # Change status of a message
    # path('contact-messages/change-message-status/<int:message_id>', views.message_status, name='mgmt-message-change-status'),
    # # Delete a request
    # path(
    #     'contact-messages/delete-message/<int:message_id>',
    #     views.message_delete,
    #     name='mgmt-message-delete'
    #     ),

    # Resident Requests list
    path('resident-requests/', views.resident_requests, name='mgmt-resident-requests'),
    # Set status to in progress
    path('resident-requests/request-in-progress/<int:resident_request_id>', views.resident_request_in_progress, name='mgmt-request-in-progress'),
    # Set status to closed
    path('resident-requests/request-closed/<int:resident_request_id>', views.resident_request_closed, name='mgmt-request-closed'),
    # Delete a request
    path(
        'resident-requests/delete-request/<int:resident_request_id>',
        views.resident_request_delete,
        name='mgmt-request-delete'
        ),

    # User accounts list
    path('user-accounts/', views.user_accounts, name='mgmt-users'),
    # Activate or deactivate user
    path('user-accounts/activation/<int:user_id>', views.user_activation, name='mgmt-user-activation'),
    # Give or Remove Admin status
    path('user-accounts/admin-status/<int:user_id>', views.user_admin_status, name='mgmt-user-admin-status'),
    # Delete a user account
    path(
        'user-accounts/delete-user/<int:user_id>',
        views.user_delete,
        name='mgmt-user-delete'
        ),
]
