from django.shortcuts import render, get_object_or_404
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.admin.views.decorators import staff_member_required
from django.urls import reverse
from django.http import HttpResponseRedirect
from dashboard.models import EventSpace, EventSpaceBooking, ResidentRequest
from contact.models import ContactMessage
from .forms import EventSpaceForm


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

    spaces_values = EventSpace.objects.all().values()

    # if request.method is GET
    return render(
        request,
        "management/event_spaces.html",
        {
            "event_spaces_values": spaces_values,
        }
    )


@staff_member_required
def event_space_bookings(request):
    """
    Display the event space bookings page

    **Context**
    ``event_space_bookings``
    An instance of :model:`EventSpaceBooking`.

    **Template:**

    :template:`management/event_space_bookings.html`
    """

    bookings = EventSpaceBooking.objects.all()

    # if request.method is GET
    return render(
        request,
        "management/event_space_bookings.html",
        {
            "event_space_bookings": bookings,
        }
    )


@staff_member_required
def resident_requests(request):
    """
    Display the resident requests page

    **Context**
    ``resident_requests``
    An instance of :model:`ResidentRequest`.

    **Template:**

    :template:`management/resident_requests.html`
    """

    res_requests = ResidentRequest.objects.all()

    # if request.method is GET
    return render(
        request,
        "management/resident_requests.html",
        {
            "resident_requests": res_requests,
        }
    )


@staff_member_required
def contact_messages(request):
    """
    Display the contact messages page

    **Context**
    ``contact_messages``
    An instance of :model:`ContactMessage`.

    **Template:**

    :template:`management/contact_messages.html`
    """

    messages = ContactMessage.objects.all()

    # if request.method is GET
    return render(
        request,
        "management/contact_messages.html",
        {
            "contact_messages": messages,
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

    # if request.method == "POST":
        # booking_form = BookingForm(data=request.POST)

        # if booking_form.is_valid():
        #     booking = booking_form.save(commit=False)
        #     booking.resident = request.user

        #     # check whether room already booked on that day
        #     if check_for_duplicate_bookings(booking, request):
        #         # Prefill form but leave date empty
        #         booking.date = ""
        #         booking_form = BookingForm(instance=booking)
        #         # render form again
        #         return render(
        #             request,
        #             "dashboard/event_space_booking.html",
        #             {
        #                 "booking_form": booking_form,
        #             }
        #         )
        #     # no duplicate bookings
        #     else:
        #         booking.save()

        #         contact_url = reverse('contact')

        #         messages.add_message(
        #             request,
        #             messages.SUCCESS,
        #             "You successfully sent a booking request. "
        #             "The request is pending and requires approval by the community administrators. "
        #             f"""If the status of your booking is still pending in 3 working days, please feel free to <a href="{contact_url}">contact us</a>."""
        #         )

        #         return HttpResponseRedirect(reverse('dashboard'))

        # # booking form not valid:
        # else:
        #     messages.add_message(
        #         request,
        #         messages.ERROR,
        #         'There was an error in your form. Please fill in again.'
        #     )

        #     return render(
        #         request,
        #         "dashboard/event_space_booking.html",
        #         {
        #             "booking_form": booking_form,
        #         }
        #     )

    # if request.method == GET
    event_space_form = EventSpaceForm()

    return render(
        request,
        "management/manage_event_spaces.html",
        {
            "event_space_form": event_space_form,
        }
    )
