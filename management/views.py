from datetime import date
from django.shortcuts import render, get_object_or_404
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.admin.views.decorators import staff_member_required
from django.urls import reverse
from django.http import HttpResponseRedirect
from dashboard.models import EventSpace, EventSpaceBooking, ResidentRequest
from contact.models import ContactMessage
from .forms import EventSpaceForm
from dashboard.utils import resident_request_type


# only for staff members to access admin page
@staff_member_required
def management_page(request):
    """
    Display the management page

    **Template:**

    :template:`management/management_page.html`
    """

    # if request.method is GET
    return render(
        request,
        "management/management_page.html",
    )


@staff_member_required
def user_accounts(request):
    """
    Display the user accounts page

    **Context**
    ``staff_users``
    ``active_users``
    ``inactive_users``
    An instance of :model:`User`.

    **Template:**

    :template:`management/users.html`
    """

    users_list = User.objects.all()

    # filter by status
    staff_users = users_list.filter(is_staff=True).order_by('username')
    active_users = users_list.filter(is_active=True, is_staff=False).order_by('username')
    inactive_users = users_list.filter(is_active=False).order_by('username')

    # Debugging output in the terminal
    print("Staff Users:", staff_users)
    print("Active Users:", active_users)
    print("Inactive Users:", inactive_users)

    # if request.method is GET
    return render(
        request,
        "management/users.html",
        {
            "staff_users": staff_users,
            "active_users": active_users,
            "inactive_users": inactive_users,
        }
    )


@staff_member_required
def user_activation(request, user_id):
    """
    Activate and deactivate user accounts

    **Template:**

    :template:`management/users.html`
    """

    # check that request.user is not accidentally changing their own status
    if user_id == request.user.id:
        messages.add_message(
                    request,
                    messages.ERROR,
                    'You cannot deactivate your own account!'
                )
    else:
        user = get_object_or_404(User, pk=user_id)

        print("user id:", user.id, user_id)
        if user.is_active:
            print("User is active, deactivate")
            user.is_active = False
        else:
            print("User is inavtive, activate")
            user.is_active = True

        user.save()

    return HttpResponseRedirect(reverse('mgmt-users'))


@staff_member_required
def user_admin_status(request, user_id):
    """
    Give and Remove Admin status to user

    **Template:**

    :template:`management/users.html`
    """
    # check that request.user is not accidentally changing their own status
    if user_id == request.user.id:
        messages.add_message(
                    request,
                    messages.ERROR,
                    'You cannot remove your own admin status!'
                )
    else:
        user = get_object_or_404(User, pk=user_id)

        print("user id:", user.id, user_id)
        if user.is_staff:
            print("User is staff, remove")
            user.is_staff = False
        else:
            print("User is not staff, give admin")
            user.is_staff = True

        user.save()

    return HttpResponseRedirect(reverse('mgmt-users'))


@staff_member_required
def user_delete(request, user_id):
    """
    view to delete user
    """
    # check that request.user is not accidentally deleting their own account
    if user_id == request.user.id:
        messages.add_message(
                    request,
                    messages.ERROR,
                    'You cannot delete your own account!'
                )
    else:
        user = get_object_or_404(User, pk=user_id)

        user.delete()
        messages.add_message(
            request,
            messages.SUCCESS,
            'User account successfully deleted!'
        )

    return HttpResponseRedirect(reverse('mgmt-users'))


@staff_member_required
def event_spaces(request):
    """
    Display the event spaces page

    **Context**
    ``event_spaces``
    An instance of :model:`EventSpace`.

    **Template:**

    :template:`management/event_spaces.html`
    """
    spaces_values = EventSpace.objects.all().values().order_by('name')

    # if request.method is GET
    return render(
        request,
        "management/event_spaces.html",
        {
            "event_spaces_values": spaces_values,
        }
    )


@staff_member_required
def add_event_space(request):
    """
    Display the add new event space page

    **Template:**

    :template:`management/mange_event_spaces.html`

    **Context:**

    ``event_space_form``
    An instance of :form:`management.EventSpaceForm`
    """

    # if method is POST
    if request.method == "POST":
        # add request.FILES to form submission since images can be uploaded
        event_space_form = EventSpaceForm(request.POST, request.FILES)

        # form is valid:
        if event_space_form.is_valid():

            event_space_form.save()

            messages.add_message(
                request,
                messages.SUCCESS,
                "You successfully added a new event space. "
            )

            return HttpResponseRedirect(reverse('mgmt-event-spaces'))

        # event space form not valid:
        else:
            messages.add_message(
                request,
                messages.ERROR,
                'There was an error in your form. Please fill in again.'
            )

            return render(
                request,
                "management/manage_event_spaces.html",
                {
                    "event_space_form": event_space_form,
                }
            )

    # if request.method is GET
    event_space_form = EventSpaceForm()

    return render(
        request,
        "management/manage_event_spaces.html",
        {
            "event_space_form": event_space_form,
        }
    )


@staff_member_required
def event_space_edit(request, space_id):
    """
    View to edit event spaces
    """
    # get event space with requested id
    space = get_object_or_404(EventSpace, pk=space_id)

    # Start if request method POST conditional
    if request.method == "POST":

        event_space_form = EventSpaceForm(request.POST, request.FILES, instance=space)

        # Start if booking has changed conditional
        if event_space_form.has_changed():

            # Start if booking form is valid conditional
            if event_space_form.is_valid():

                event_space_form.save()

                # add success message
                messages.add_message(
                    request,
                    messages.SUCCESS,
                    "Event Space was successfully updated!"
                )

                return HttpResponseRedirect(reverse('mgmt-event-spaces'))

            # booking form not valid
            else:
                messages.add_message(
                    request,
                    messages.ERROR,
                    'Error updating event space!'
                )

                return render(
                    request,
                    "management/manage_event_spaces.html",
                    {
                        "event_space_form": event_space_form,
                    }
                )
            # End event space form valid conditional

        # No fields have changed
        else:
            messages.add_message(
                request,
                messages.INFO,
                'No changes were made to the event space.'
            )

            return HttpResponseRedirect(reverse('mgmt-event-spaces'))
        # End event space form changed conditional

    # If request.method is GET
    else:
        event_space_form = EventSpaceForm(instance=space)

        return render(
            request,
            "management/manage_event_spaces.html",
            {
                "event_space_form": event_space_form,
            }
        )
    # End request.method POST conditional


@staff_member_required
def event_space_delete(request, space_id):
    """
    view to delete event space
    """
    space = get_object_or_404(EventSpace, pk=space_id)
    space.delete()

    messages.add_message(
        request,
        messages.SUCCESS,
        'Event Space successfully deleted!'
    )

    return HttpResponseRedirect(reverse('mgmt-event-spaces'))


@staff_member_required
def event_space_bookings(request):
    """
    Display the event space bookings page

    **Context**
    ``pending_bookings``
    An instance of :model:`EventSpaceBooking` with status 0.
    ``approved_bookings``
    An instance of :model:`EventSpaceBooking` with status 1.
    ``denied_bookings``
    An instance of :model:`EventSpaceBooking` with status 2.
    ``past_bookings``
    An instance of :model:`EventSpaceBooking` with a date in the past.

    **Template:**

    :template:`management/event_space_bookings.html`
    """

    bookings = EventSpaceBooking.objects.all().order_by("date")

    # sort into past and future bookings
    past_bookings = bookings.filter(date__lt=date.today())
    future_bookings = bookings.exclude(date__lt=date.today())

    # sort bookings by status
    pending_bookings = future_bookings.filter(status=0)
    approved_bookings = future_bookings.filter(status=1)
    denied_bookings = future_bookings.filter(status=2)

    # if request.method is GET
    return render(
        request,
        "management/event_space_bookings.html",
        {
            "pending_bookings": pending_bookings,
            "approved_bookings": approved_bookings,
            "denied_bookings": denied_bookings,
            "past_bookings": past_bookings,
        }
    )


@staff_member_required
def approve_booking(request, booking_id):
    """
    Approve booking requests

    **Template:**

    :template:`management/event_space_bookings.html`
    """

    booking = get_object_or_404(EventSpaceBooking, pk=booking_id)

    # check whether booking.date is not in the past
    if booking.date < date.today():
        messages.add_message(
            request,
            messages.ERROR,
            'You cannot change the status of past bookings!'
        )

        return HttpResponseRedirect(reverse('mgmt-event-space-bookings'))

    # check whether booking is not already approved
    if booking.status == 1:
        messages.add_message(
                    request,
                    messages.INFO,
                    'This booking was already approved!'
                )
    else:
        booking.status = 1

        messages.add_message(
            request,
            messages.SUCCESS,
            'Booking successfully approved!'
        )

        booking.save()

    return HttpResponseRedirect(reverse('mgmt-event-space-bookings'))


@staff_member_required
def deny_booking(request, booking_id):
    """
    Deny booking requests

    **Template:**

    :template:`management/event_space_bookings.html`
    """

    booking = get_object_or_404(EventSpaceBooking, pk=booking_id)

    # check whether booking.date is not in the past
    if booking.date < date.today():
        messages.add_message(
            request,
            messages.ERROR,
            'You cannot change the status of past bookings!'
        )

        return HttpResponseRedirect(reverse('mgmt-event-space-bookings'))

    # check whether booking is not already denied
    if booking.status == 2:
        messages.add_message(
                    request,
                    messages.INFO,
                    'This booking was already denied!'
                )
    else:
        booking.status = 2

        messages.add_message(
                    request,
                    messages.SUCCESS,
                    'Booking successfully denied!'
                )

        booking.save()

    return HttpResponseRedirect(reverse('mgmt-event-space-bookings'))


@staff_member_required
def booking_delete(request, booking_id):
    """
    view to delete event space booking
    """
    booking = get_object_or_404(EventSpaceBooking, pk=booking_id)
    booking.delete()

    messages.add_message(
        request,
        messages.SUCCESS,
        'Booking successfully deleted!'
    )

    return HttpResponseRedirect(reverse('mgmt-event-space-bookings'))


@staff_member_required
def resident_requests(request):
    """
    Display the resident requests page

    **Context**
    ``open_maintenance_requests``
    An instance of :model:`ResidentRequest` with purpose 0 and status 0
    ``progress_maintenance_requests``
    An instance of :model:`ResidentRequest` with purpose 0 and status 1
    ``closed_maintenance_requests``
    An instance of :model:`ResidentRequest` with purpose 0 and status 2
    ``open_messages``
    An instance of :model:`ResidentRequest` with purpose 1 and status 0
    ``progress_messages``
    An instance of :model:`ResidentRequest` with purpose 1 and status 1
    ``closed_messages``
    An instance of :model:`ResidentRequest` with purpose 1 and status 2

    **Template:**

    :template:`management/resident_requests.html`
    """

    res_requests = ResidentRequest.objects.all().order_by("created_on")

    # filter maintenance requests and sort by status
    open_maintenance_requests = res_requests.filter(purpose=0, status=0)
    progress_maintenance_requests = res_requests.filter(purpose=0, status=1)
    closed_maintenance_requests = res_requests.filter(purpose=0, status=2)

    # filter messages and sort by status
    open_messages = res_requests.filter(purpose=1, status=0)
    progress_messages = res_requests.filter(purpose=1, status=1)
    closed_messages = res_requests.filter(purpose=1, status=2)

    # if request.method is GET
    return render(
        request,
        "management/resident_requests.html",
        {
            "open_maintenance_requests": open_maintenance_requests,
            "progress_maintenance_requests": progress_maintenance_requests,
            "closed_maintenance_requests": closed_maintenance_requests,
            "open_messages": open_messages,
            "progress_messages": progress_messages,
            "closed_messages": closed_messages,
        }
    )


@staff_member_required
def resident_request_in_progress(request, resident_request_id):
    """
    Set resident requests status to in progress

    **Template:**

    :template:`management/resident_requests.html`
    """

    resident_request = get_object_or_404(
                        ResidentRequest,
                        pk=resident_request_id
                        )

    # check whether request is not already in progress
    if resident_request.status == 1:
        messages.add_message(
                    request,
                    messages.INFO,
                    f"This {resident_request_type(resident_request.purpose).lower()} is already in progress!"  # noqa
                )
    else:
        resident_request.status = 1

        messages.add_message(
            request,
            messages.SUCCESS,
            f"{resident_request_type(resident_request.purpose)} "
            "successfully set to 'In Progress'!"
        )

        resident_request.save()

    return HttpResponseRedirect(reverse('mgmt-resident-requests'))


@staff_member_required
def resident_request_closed(request, resident_request_id):
    """
    Set resident request status to closed

    **Template:**

    :template:`management/resident_requests.html`
    """

    resident_request = get_object_or_404(
                        ResidentRequest,
                        pk=resident_request_id
                        )

    # check whether request is not already closed
    if resident_request.status == 2:
        messages.add_message(
                    request,
                    messages.INFO,
                    f"This {resident_request_type(resident_request.purpose).lower()} was already closed!"  # noqa
                )
    else:
        resident_request.status = 2

        messages.add_message(
            request,
            messages.SUCCESS,
            f"{resident_request_type(resident_request.purpose)} "
            "successfully closed!"
        )

        resident_request.save()

    return HttpResponseRedirect(reverse('mgmt-resident-requests'))


@staff_member_required
def resident_request_delete(request, resident_request_id):
    """
    view to delete resident request
    """
    resident_request = get_object_or_404(
                            ResidentRequest,
                            pk=resident_request_id
                            )
    resident_request.delete()

    messages.add_message(
        request,
        messages.SUCCESS,
        f"{resident_request_type(resident_request.purpose)} "
        "successfully deleted!"
    )

    return HttpResponseRedirect(reverse('mgmt-resident-requests'))


@staff_member_required
def contact_messages(request):
    """
    Display the contact messages page

    **Context**
    ``open_contact_messages``
    An instance of :model:`ContactMessage` with processed False.
    ``processed_contact_messages``
    An instance of :model:`ContactMessage` with processed True.

    **Template:**

    :template:`management/contact_messages.html`
    """

    messages = ContactMessage.objects.all().order_by("-sent_on")

    # sort by whether processed or not
    open_messages = messages.filter(processed=False)
    processed_messages = messages.filter(processed=True)

    # if request.method is GET
    return render(
        request,
        "management/contact_messages.html",
        {
            "open_contact_messages": open_messages,
            "processed_contact_messages": processed_messages,
        }
    )


@staff_member_required
def message_processed(request, message_id):
    """
    Set contact message status to processed

    **Template:**

    :template:`management/contact_messages.html`
    """
    print("processed")

    message = get_object_or_404(ContactMessage, pk=message_id)

    # check whether message is not already processed
    if message.processed:
        messages.add_message(
                    request,
                    messages.INFO,
                    f"This message was already processed!"  # noqa
                )
    else:
        message.processed = True

        messages.add_message(
            request,
            messages.SUCCESS,
            "The message was successfully set to 'Processed'!"
        )

        message.save()

    return HttpResponseRedirect(reverse('mgmt-contact-messages'))


@staff_member_required
def message_delete(request, message_id):
    """
    view to delete contact message
    """
    message = get_object_or_404(
                            ContactMessage,
                            pk=message_id
                            )
    message.delete()

    messages.add_message(
        request,
        messages.SUCCESS,
        "The message was successfully deleted!"
    )

    return HttpResponseRedirect(reverse('mgmt-contact-messages'))
