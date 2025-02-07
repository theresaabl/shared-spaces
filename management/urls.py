from . import views
from django.urls import path

urlpatterns = [
    path('', views.management_page, name='management'),
    path('user-accounts/', views.user_accounts, name='users'),
]
