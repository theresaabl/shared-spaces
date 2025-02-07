from django.shortcuts import render, get_object_or_404
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.admin.views.decorators import staff_member_required
from django.urls import reverse
from django.http import HttpResponseRedirect


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
    ``users``
    An instance of :model:`User`.

    **Template:**

    :template:`management/users.html`
    """

    users_list = User.objects.all()

    # if request.method is GET
    return render(
        request,
        "management/users.html",
        {
            "users_list": users_list,
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

    return HttpResponseRedirect(reverse('users'))


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

    return HttpResponseRedirect(reverse('users'))


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

    return HttpResponseRedirect(reverse('users'))
