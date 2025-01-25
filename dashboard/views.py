from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def resident_dashboard(request):
    """
    Display the resident space page

    **Template:**

    :template:`dashboard/resident_space.html`
    """

    return render(
        request,
        "dashboard/resident_space.html",
    )


def event_space_booking(request):
    """
    Display the event space booking page

    **Template:**

    :template:`dashboard/event_space_booking.html`
    """

    return render(
        request,
        "dashboard/event_space_booking.html",
    )
