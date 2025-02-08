from . import views
from django.urls import path

urlpatterns = [
    path('', views.management_page, name='management'),
    path('event-spaces/', views.event_spaces, name='mgmt-event-spaces'),
    path('event-spaces/manage-event-spaces', views.add_event_space, name='mgmt-add-event-space'),
    path('event-space-bookings/', views.event_space_bookings, name='mgmt-event-space-bookings'),
    path('contact-messages/', views.contact_messages, name='mgmt-contact-messages'),
    path('resident-requests/', views.resident_requests, name='mgmt-resident-requests'),
    path('user-accounts/', views.user_accounts, name='mgmt-users'),
    path('user-accounts/activation/<int:user_id>', views.user_activation, name='mgmt-user-activation'),
    path('user-accounts/admin-status/<int:user_id>', views.user_admin_status, name='mgmt-user-admin-status'),
    path(
        'user-accounts/delete-user/<int:user_id>',
        views.user_delete,
        name='mgmt-user-delete'
        ),
]
