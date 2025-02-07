from django.contrib import messages
from .models import EventSpaceBooking


def check_for_duplicate_bookings(booking, request):
    """
    Helper function for event_space_booking and booking_edit
    check whether room already booked on that day,
    before current booking is saved to db
    if there is a duplicate booking:
    return message and render prefilled form with empty date field
    """
    print("check for duplicate bookings")
    duplicate_bookings = EventSpaceBooking.objects.filter(
                            event_space=booking.event_space,
                            date=booking.date
                            ).exclude(id=booking.id)

    print(duplicate_bookings)
    if duplicate_bookings:
        print("inside if duplicate_bookings")
        messages.add_message(
            request,
            messages.ERROR,
            'This event space is already booked on the requested day! '
            'Please choose another room or date.'
        )
        print("message added")

        return True
    print("return none from duplicate bookings")
    return False


def resident_request_type(purpose):
    """
    Helper function for edit_resident_request and delete_resident_request views
    Returns whether the resident request is of type request or message
    """
    return "Maintenance request" if purpose == 0 else "Message"


def convert_date(booking_date):
    """
    Convert date to 'YYYY-MM-DD' for proper display in date picker
    """
    return booking_date.strftime("%Y-%m-%d")
