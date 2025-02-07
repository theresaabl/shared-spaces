from . import views
from django.urls import path

urlpatterns = [
    path('', views.management_page, name='management'),
    path('user-accounts/', views.user_accounts, name='users'),
    path('user-accounts/activation/<int:user_id>', views.user_activation, name='user-activation'),
    path('user-accounts/admin-status/<int:user_id>', views.user_admin_status, name='user-admin-status'),
]
