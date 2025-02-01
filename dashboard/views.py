from django.shortcuts import render, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from django.http import HttpResponseRedirect
from .models import EventSpaceBooking, EventSpace, ResidentRequest
from .forms import BookingForm, ResidentRequestForm
from .utils import check_for_duplicate_bookings, resident_request_type


def resident_dashboard(request):
    """
    Display the resident space page

        **Context**

    ``event_space_booking``
        An instance of :model:`dashboard.EventSpaceBooking`.

    ``resident_request``
        An instance of :model:`dashboard.ResidentRequest`.

    **Template:**

    :template:`dashboard/resident_space.html`
    """

    # get all event space bookings for the current user
    # to do: order by date #############
    # check whether user is logged in or not before database request of bookings and resident requests
    # do not user login_required decorator here because want to display content from resident_space template
    if request.user.is_authenticated:
        event_space_bookings = EventSpaceBooking.objects.filter(resident=request.user)  # noqa
        resident_requests = ResidentRequest.objects.filter(resident=request.user)  # noqa
    else:
        # empty when user is not logged in, because still need to render template
        event_space_bookings = ""
        resident_requests = ""

    return render(
        request,
        "dashboard/resident_space.html",
        {
            "event_space_bookings": event_space_bookings,
            "resident_requests": resident_requests,
        }
    )


@login_required
def event_space_booking(request, space_id=None):
    """
    Display the event space booking page

    Optional space_id parameter: if included: book specific event space

    **Template:**

    :template:`dashboard/event_space_booking.html`

    **Context:**

    ``booking_form``
    An instance of :form:`dashboard.BookingForm`
    """

    if request.method == "POST":
        booking_form = BookingForm(data=request.POST)

        if booking_form.is_valid():
            booking = booking_form.save(commit=False)
            booking.resident = request.user

            # check whether room already booked on that day
            if not check_for_duplicate_bookings(booking, request):
                booking.save()

                contact_url = reverse('contact')

                messages.add_message(
                    request,
                    messages.SUCCESS,
                    "You successfully sent a booking request. "
                    "The request is pending and requires approval by the community administrators. "
                    f"""If the status of your booking is still pending in 3 working days, please feel free to <a href="{contact_url}">contact us</a>."""
                )

                return HttpResponseRedirect(reverse('dashboard'))

        # booking form not valid:
        else:
            messages.add_message(
                request,
                messages.ERROR,
                'There was an error in your form. Please fill in again.'
            )

            return render(
                request,
                "dashboard/event_space_booking.html",
                {
                    "booking_form": booking_form,
                }
            )

    # if request.method == GET
    booking_form = BookingForm()

    # If user wants to book a specific room (when coming from event space list page)
    if space_id:
        # get instance of event space with given id
        event_space = get_object_or_404(EventSpace, id=space_id)

        booking = booking_form.save(commit=False)
        booking.event_space = event_space
        # prefill the event space field
        booking_form = BookingForm(instance=booking)

    return render(
        request,
        "dashboard/event_space_booking.html",
        {
            "booking_form": booking_form,
        }
    )


@login_required
def booking_edit(request, booking_id):
    """
    View to edit event space bookings
    """
    # get booking with requested id
    booking = get_object_or_404(EventSpaceBooking, pk=booking_id)

    # check whether request.user is the user who made the booking
    if not request.user == booking.resident:
        messages.add_message(
            request,
            messages.ERROR,
            'You do not have access to this booking.'
        )

        return HttpResponseRedirect(reverse('dashboard'))

    if request.method == "POST":

        booking_form = BookingForm(data=request.POST, instance=booking)

        if booking_form.is_valid():
            booking = booking_form.save(commit=False)

            if not check_for_duplicate_bookings(booking, request):

                # add logic: if all you change is notes: status can stay, if change date, time or space: reset
                booking.status = 0
                booking.save()
                messages.add_message(
                    request,
                    messages.SUCCESS,
                    'Event space booking successfully updated! Waiting for approval.'
                )

                return HttpResponseRedirect(reverse('dashboard'))
        else:
            messages.add_message(
                request,
                messages.ERROR,
                'Error updating event space booking!'
            )

            return render(
                request,
                "dashboard/event_space_booking.html",
                {
                    "booking_form": booking_form,
                }
            )

    else:
        booking_form = BookingForm(instance=booking)

        return render(
            request,
            "dashboard/event_space_booking.html",
            {
                "booking_form": booking_form,
            }
        )


@login_required
def booking_delete(request, booking_id):
    """
    view to delete booking
    """
    # get booking with requested id
    booking = get_object_or_404(EventSpaceBooking, pk=booking_id)

    # check whether request.user is the user who made the booking
    if not request.user == booking.resident:
        messages.add_message(
            request,
            messages.ERROR,
            'You do not have access to this booking.'
        )

        return HttpResponseRedirect(reverse('dashboard'))

    booking.delete()
    messages.add_message(
        request,
        messages.SUCCESS,
        'Event Space Booking successfully deleted!'
    )

    return HttpResponseRedirect(reverse('dashboard'))


@login_required
def event_spaces_list(request):
    """
    Display a page with a list of event spaces

    **Context**

    ``event_spaces``
        An instance of :model:`dashboard.EventSpace`.

    **Template:**

    :template:`dashboard/event_spaces_list.html`
    """
    # get key value pairs for all fields of all event spaces
    event_spaces_values = EventSpace.objects.all().values()

    return render(
        request,
        "dashboard/event_spaces_list.html",
        {
            "event_spaces_values": event_spaces_values,
        }
    )


@login_required
def submit_request(request):
    """
    Display the resident request submission page

    **Template:**

    :template:`dashboard/submit_request.html`

    **Context:**

    ``resident_request_form``
    An instance of :form:`dashboard.ResidentRequestForm`
    """

    if request.method == "POST":
        resident_request_form = ResidentRequestForm(data=request.POST)

        if resident_request_form.is_valid():
            resident_request = resident_request_form.save(commit=False)
            resident_request.resident = request.user

            resident_request.save()

            contact_url = reverse('contact')

            messages.add_message(
                request,
                messages.SUCCESS,
                'You successfully sent a '
                f'{resident_request_type(resident_request.purpose).lower()}. '
                'If you do not hear back within 3 working days, please '
                f"""feel free to <a href="{contact_url}">contact us</a>."""
            )

            return HttpResponseRedirect(reverse('dashboard'))

        # booking form not valid:
        else:
            messages.add_message(
                request,
                messages.ERROR,
                'There was an error in your form. Please fill in again.'
            )

            return render(
                request,
                "dashboard/submit_request.html",
                {
                    "resident_request_form": resident_request_form,
                }
            )

    # if request.method == GET
    resident_request_form = ResidentRequestForm()

    return render(
        request,
        "dashboard/submit_request.html",
        {
            "resident_request_form": resident_request_form,
        }
    )


@login_required
def resident_request_edit(request, resident_request_id):
    """
    View to edit resident requests
    """
    # get resident request with requested id
    resident_request = get_object_or_404(
                            ResidentRequest,
                            pk=resident_request_id
                        )

    # check whether request.user is the user who made the resident request
    if not request.user == resident_request.resident:
        messages.add_message(
            request,
            messages.ERROR,
            'You do not have access to this '
            f'{resident_request_type(resident_request.purpose).lower()}.'
        )

        return HttpResponseRedirect(reverse('dashboard'))

    if request.method == "POST":

        resident_request_form = ResidentRequestForm(
                                    data=request.POST,
                                    instance=resident_request
                                )

        if resident_request_form.is_valid():
            resident_request = resident_request_form.save(commit=False)

            resident_request.status = 0
            resident_request.save()
            messages.add_message(
                request,
                messages.SUCCESS,
                f'{resident_request_type(resident_request.purpose)} '
                'successfully updated! Waiting for approval.'
            )

            return HttpResponseRedirect(reverse('dashboard'))

        else:
            messages.add_message(
                request,
                messages.ERROR,
                'Error updating '
                f'{resident_request_type(resident_request.purpose).lower()}.'
            )

            return render(
                request,
                "dashboard/submit_request.html",
                {
                    "resident_request_form": resident_request_form,
                }
            )

    else:
        resident_request_form = ResidentRequestForm(instance=resident_request)

        return render(
            request,
            "dashboard/submit_request.html",
            {
                "resident_request_form": resident_request_form,
            }
        )


@login_required
def resident_request_delete(request, resident_request_id):
    """
    view to delete resident request
    """
    # get resident request with requested id
    resident_request = get_object_or_404(
                            ResidentRequest,
                            pk=resident_request_id
                        )

    # check whether request.user is the user who made the resident request
    if not request.user == resident_request.resident:
        messages.add_message(
            request,
            messages.ERROR,
            'You do not have access to this '
            f'{resident_request_type(resident_request.purpose).lower()}.'
        )

        return HttpResponseRedirect(reverse('dashboard'))

    resident_request.delete()
    messages.add_message(
        request,
        messages.SUCCESS,
        f'{resident_request_type(resident_request.purpose)} '
        'successfully deleted!'
    )

    return HttpResponseRedirect(reverse('dashboard'))
