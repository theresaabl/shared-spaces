from django.contrib import admin
from .models import ContactMessage


@admin.register(ContactMessage)
class ContactAdmin(admin.ModelAdmin):
    """
    Register ContactMessage model to admin panel
    Customize display, search fields and filter
    """
    list_display = (
                    "name",
                    "email",
                    "interest_to_join",
                    "sent_on",
                    "processed"
                    )
    search_fields = ["name", "message"]
    list_filter = ("processed", "interest_to_join")
