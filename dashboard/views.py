from django.shortcuts import render
from .forms import BookingForm


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

    **Context:**

    ``booking_form``
    An instance of :form:`blog.BookingForm`
    """

    booking_form = BookingForm()

    return render(
        request,
        "dashboard/event_space_booking.html",
        {
            "booking_form": booking_form,
        }
    )
