from django.shortcuts import render
from django.contrib import messages
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
    if request.method == "POST":
        booking_form = BookingForm(data=request.POST)
        if booking_form.is_valid():
            booking = booking_form.save(commit=False)
            booking.resident = request.user
            booking.save()
            messages.add_message(
                request,
                messages.SUCCESS,
                "You successfully sent a booking request. "
                "The request is pending and requires approval by the community administrators. "
                """If the status of your booking is still pending in 3 working days, please feel free to <a href="#">contact us</a>."""
            )

    booking_form = BookingForm()

    return render(
        request,
        "dashboard/event_space_booking.html",
        {
            "booking_form": booking_form,
        }
    )
