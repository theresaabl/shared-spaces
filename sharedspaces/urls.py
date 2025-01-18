"""
URL configuration for sharedspaces project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from dashboard.views import resident_dashboard
from main.views import about_page
from contact.views import contact_page

urlpatterns = [
    path('about/', about_page, name='about'),
    path('accounts/', include('allauth.urls')),
    path('admin/', admin.site.urls),
    path('contact/', contact_page, name='contact'),
    path('dashboard/', resident_dashboard, name='dashboard'),
    path('', include('main.urls'), name='main-urls'),
]
