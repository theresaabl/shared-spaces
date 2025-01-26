from django.shortcuts import render
from django.contrib import messages
from django.urls import reverse
from .models import EventSpaceBooking
from .forms import BookingForm


# Create your views here.
def resident_dashboard(request):
    """
    Display the resident space page

        **Context**

    ``event_space_booking``
        An instance of :model:`blog.EventSpaceBooking`.

    **Template:**

    :template:`dashboard/resident_space.html`
    """

    # get all event space bookings for the current user
    # to do: order by date
    event_space_bookings = EventSpaceBooking.objects.filter(resident=request.user)  # noqa

    return render(
        request,
        "dashboard/resident_space.html",
        {
            "event_space_bookings": event_space_bookings,
        }
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
    if request.method == "POST":
        booking_form = BookingForm(data=request.POST)
        if booking_form.is_valid():
            booking = booking_form.save(commit=False)
            booking.resident = request.user
            booking.save()

            contact_url = reverse('contact')

            messages.add_message(
                request,
                messages.SUCCESS,
                "You successfully sent a booking request. "
                "The request is pending and requires approval by the community administrators. "
                f"""If the status of your booking is still pending in 3 working days, please feel free to <a href="{contact_url}">contact us</a>."""
            )

    booking_form = BookingForm()

    return render(
        request,
        "dashboard/event_space_booking.html",
        {
            "booking_form": booking_form,
        }
    )
