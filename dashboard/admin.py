from django.contrib import admin
from .models import EventSpace, EventSpaceBooking, ResidentRequest


@admin.register(EventSpace)
class EventSpaceAdmin(admin.ModelAdmin):
    """
    Register EventSpace model to admin panel
    Customize display, search fields and filter
    """
    list_display = (
                    "name",
                    "type",
                    "building",
                    "capacity",
                    )
    search_fields = ["name", "type"]
    list_filter = ("type",)


@admin.register(EventSpaceBooking)
class EventSpaceBookingAdmin(admin.ModelAdmin):
    """
    Register EventSpaceBooking model to admin panel
    Customize display, search fields and filter
    """
    list_display = (
                    "resident",
                    "event_space",
                    "date",
                    "start",
                    "end",
                    "created_on",
                    "status"
                    )
    search_fields = ["resident", "event_space", "date"]
    list_filter = ("status",)


@admin.register(ResidentRequest)
class ResidentRequestAdmin(admin.ModelAdmin):
    """
    Register ResidentRequest model to admin panel
    Customize display, search fields and filter
    """
    list_display = (
                    "resident",
                    "purpose",
                    "urgent",
                    "created_on",
                    "status"
                    )
    search_fields = ["resident", "content"]
    list_filter = ("purpose", "status")
