from django.contrib import admin
from .models import EventSpace, EventSpaceBooking, ResidentRequest

admin.site.register(EventSpace)

admin.site.register(EventSpaceBooking)

admin.site.register(ResidentRequest)
