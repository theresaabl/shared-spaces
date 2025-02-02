from . import views
from django.urls import path

urlpatterns = [
    path('', views.management_page, name='management'),
]
