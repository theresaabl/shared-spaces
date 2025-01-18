from . import views
from django.urls import path

urlpatterns = [
    path('', views.resident_dashboard, name='dashboard'),
]
