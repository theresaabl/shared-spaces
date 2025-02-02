"""
URL configuration for sharedspaces project.
"""
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('accounts/', include('allauth.urls')),
    path('admin/', admin.site.urls),
    path('contact/', include('contact.urls'), name='contact-urls'),
    path('dashboard/', include('dashboard.urls'), name='dashboard-urls'),
    path('management/', include('management.urls'), name='management-urls'),
    path('', include('main.urls'), name='main-urls'),
]
