from django.shortcuts import render
from django.contrib import messages
from .models import EventSpaceBooking
from .forms import BookingForm


def check_for_duplicate_bookings(booking, request):
    """
    Helper function for event_space_booking and booking_edit
    check whether room already booked on that day,
    before current booking is saved to db
    if there is a duplicate booking:
    return message and render prefilled form with empty date field
    """
    duplicate_bookings = EventSpaceBooking.objects.filter(
                            event_space=booking.event_space,
                            date=booking.date
                            )

    if duplicate_bookings:
        messages.add_message(
            request,
            messages.ERROR,
            'This event space is already booked on the requested day! '
            'Please choose another date.'
        )
        # Prefill form but leave date empty
        booking.date = ""
        booking_form = BookingForm(instance=booking)
        return render(
                    request,
                    "dashboard/event_space_booking.html",
                    {
                        "booking_form": booking_form,
                    }
                )
    return None
