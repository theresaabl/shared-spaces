from django.shortcuts import render, get_object_or_404
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

    **Context**
    ``users``
    An instance of :model:`User`.

    **Template:**

    :template:`management/users.html`
    """

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
