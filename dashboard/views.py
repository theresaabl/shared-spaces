from allauth.account.views import LoginView
from django.shortcuts import render, get_object_or_404
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth.hashers import check_password
from django.urls import reverse
from django.http import HttpResponseRedirect
from .models import EventSpaceBooking, EventSpace, ResidentRequest
from .forms import BookingForm, ResidentRequestForm
from .utils import check_for_duplicate_bookings, resident_request_type, convert_date


class MyCustomLoginView(LoginView):

    def post(self, request, *args, **kwargs):
        # Get the login credentials from the form
        username = request.POST.get('login')
        password = request.POST.get('password')

        # Check whether user exists
        try:
            # Try to get user by username
            user = User.objects.get(username=username)
        except User.DoesNotExist:
            user = None

        # if username exists and the input password matches the stored hash
        if user and check_password(password, user.password):
            # if user is not active (yet)
            if not user.is_active:
                # If user is authenticated but inactive, show inactive page
                return render(
                    request,
                    "../templates/account/account_inactive.html",
                    )

        # call the original post method from the LoginView to continue normal login flow
        return super().post(request, *args, **kwargs)


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
            if check_for_duplicate_bookings(booking, request):
                # Prefill form but leave date empty
                booking.date = ""
                booking_form = BookingForm(instance=booking)
                # render form again
                return render(
                    request,
                    "dashboard/event_space_booking.html",
                    {
                        "booking_form": booking_form,
                    }
                )
            # no duplicate bookings
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

    # save the original date and event space in case of duplicate booking after edit
    old_date = convert_date(booking.date)
    old_event_space = booking.event_space

    # check whether request.user is the user who made the booking
    if not request.user == booking.resident:
        messages.add_message(
            request,
            messages.ERROR,
            'You do not have access to this booking.'
        )

        return HttpResponseRedirect(reverse('dashboard'))

    # Start if request method POST conditional
    if request.method == "POST":

        booking_form = BookingForm(data=request.POST, instance=booking)

        # Start if booking has changed conditional
        if booking_form.has_changed():

            # Start if booking form is valid conditional
            if booking_form.is_valid():
                print("booking form is valid")

                print("old date:", old_date)
                booking = booking_form.save(commit=False)

                print("booking form has changed", booking_form.has_changed())

                # Save which fields have changed
                changed_fields = booking_form.changed_data
                print("changed fields:", changed_fields)

                # Start if date has changed conditional
                if 'date' in changed_fields:
                    # Start if date has changed and check for duplicate bookings conditional
                    if check_for_duplicate_bookings(booking, request):
                        print("inside check for duplicate bookings loop in views")
                        # Prefill form but leave original date
                        booking.date = old_date
                        booking_form = BookingForm(instance=booking)
                        # render form again
                        return render(
                            request,
                            "dashboard/event_space_booking.html",
                            {
                                "booking_form": booking_form,
                            }
                        )
                    # End if date changed and check for duplicate bookings conditional

                # if Date has not changed:
                else:
                    # Start if event space has changed conditional
                    if 'event_space' in changed_fields:
                        # Start if event space has changed and check for duplicate bookings conditional
                        if check_for_duplicate_bookings(booking, request):
                            print("inside check for duplicate bookings loop in views")
                            # Prefill form but leave original event space
                            booking.event_space = old_event_space
                            booking.date = convert_date(booking.date)
                            booking_form = BookingForm(instance=booking)
                            # render form again
                            return render(
                                request,
                                "dashboard/event_space_booking.html",
                                {
                                    "booking_form": booking_form,
                                }
                            )
                        # End if event space changed and check for duplicate bookings conditional

                # Continue if date and event space not changed or no duplicate bookings on that date
                print("booking not duplicate")

                # if all you change is notes or occasion: status can stay, if change date, time or space: reset status and wait for approval again.
                if 'event_space' in changed_fields or 'date' in changed_fields or 'start' in changed_fields or 'end' in changed_fields:
                    booking.status = 0
                    contact_url = reverse('contact')
                    booking_edited_success_message = f"""Your booking was successfully updated!
                    The request is pending again and requires approval by the community administrators.
                    If the status of your booking is still pending in 3 working days, please feel free to <a href="{contact_url}">contact us</a>."""
                else:
                    booking_edited_success_message = "Your booking was successfully updated!"

                print("booking saved")
                # save edited booking
                booking.save()
                # add success message
                messages.add_message(
                    request,
                    messages.SUCCESS,
                    booking_edited_success_message
                )
                print("message added")

                return HttpResponseRedirect(reverse('dashboard'))

            # booking form not valid
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
            # End booking form valid conditional

        # No fields have changed
        else:
            messages.add_message(
                request,
                messages.INFO,
                'No changes were made to your booking.'
            )
            print("message added")

            return HttpResponseRedirect(reverse('dashboard'))
        # End booking form changed conditional

    # If request.method is GET
    else:
        # convert date to proper format for HTML date picker
        booking.date = convert_date(booking.date)
        booking_form = BookingForm(instance=booking)

        return render(
            request,
            "dashboard/event_space_booking.html",
            {
                "booking_form": booking_form,
            }
        )
    # End request.method POST conditional


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

    # Start request.method is POST conditional
    if request.method == "POST":

        resident_request_form = ResidentRequestForm(
                                    data=request.POST,
                                    instance=resident_request
                                )

        # Start if resident_request has changed conditional
        if resident_request_form.has_changed():

            # Start form is valid conditional
            if resident_request_form.is_valid():
                resident_request = resident_request_form.save(commit=False)

                resident_request.status = 0
                resident_request.save()

                contact_url = reverse('contact')
                messages.add_message(
                    request,
                    messages.SUCCESS,
                    'You successfully updated your '
                    f'{resident_request_type(resident_request.purpose).lower()}. '
                    'If you do not hear back within 3 working days, please '
                    f"""feel free to <a href="{contact_url}">contact us</a>."""
                )

                return HttpResponseRedirect(reverse('dashboard'))

            # form is not valid
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
            # End form is valid conditional

        # No fields have changed
        else:
            messages.add_message(
                request,
                messages.INFO,
                'No changes were made to your '
                f'{resident_request_type(resident_request.purpose).lower()}.'
            )

            return HttpResponseRedirect(reverse('dashboard'))
        # End form has changed conditional

    # if request.method is GET
    else:
        resident_request_form = ResidentRequestForm(instance=resident_request)

        return render(
            request,
            "dashboard/submit_request.html",
            {
                "resident_request_form": resident_request_form,
            }
        )
    # End request.method is POST conditional


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
