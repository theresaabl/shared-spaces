from django.shortcuts import render, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from django.http import HttpResponseRedirect
from .models import EventSpaceBooking, EventSpace
from .forms import BookingForm


def resident_dashboard(request):
    """
    Display the resident space page

        **Context**

    ``event_space_booking``
        An instance of :model:`dashboard.EventSpaceBooking`.

    **Template:**

    :template:`dashboard/resident_space.html`
    """

    # get all event space bookings for the current user
    # to do: order by date
    # check whether user is logged in or not before database request of bookings
    # do not user login_required decorator here because want to display content from resident_space template
    if request.user.is_authenticated:
        event_space_bookings = EventSpaceBooking.objects.filter(resident=request.user)  # noqa
    else:
        event_space_bookings = ""

    return render(
        request,
        "dashboard/resident_space.html",
        {
            "event_space_bookings": event_space_bookings,
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
            same_day_bookings = EventSpaceBooking.objects.filter(event_space=booking.event_space, date=booking.date)

            if same_day_bookings:
                messages.add_message(
                    request,
                    messages.ERROR,
                    'This event space is already booked on the requested day! Please choose another date.'
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

            else:
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
                'There was an error in your form. Please fill in again and make sure your input is valid.'
            )

            return HttpResponseRedirect(reverse('booking'))

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

    queryset = EventSpaceBooking.objects.filter(resident=request.user)
    booking = get_object_or_404(queryset, pk=booking_id)

    if request.method == "POST":

        booking_form = BookingForm(data=request.POST, instance=booking)

        if booking_form.is_valid():
            booking = booking_form.save(commit=False)
            # add logic: if all you change is notes: status can stay, if change date, time or space: reset
            booking.status = 0
            booking.save()
            messages.add_message(
                request,
                messages.SUCCESS,
                'Event space booking successfully updated! Waiting for approval.'
            )
        else:
            messages.add_message(
                request,
                messages.ERROR,
                'Error updating event space booking!'
            )

        return HttpResponseRedirect(reverse('dashboard'))

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
    queryset = EventSpaceBooking.objects.filter(resident=request.user)
    booking = get_object_or_404(queryset, pk=booking_id)

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

    event_spaces = EventSpace.objects.all()
    event_spaces_values = event_spaces.values()

    return render(
        request,
        "dashboard/event_spaces_list.html",
        {
            "event_spaces": event_spaces,
            "event_spaces_values": event_spaces_values,
        }
    )
