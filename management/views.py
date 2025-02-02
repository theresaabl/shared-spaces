from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.admin.views.decorators import staff_member_required
from django.urls import reverse
from django.http import HttpResponseRedirect


# only for staff members to access admin page
@staff_member_required
def management_page(request):
    """
    Display the management page

    **Context**

    **Template:**

    :template:`management/management_page.html`
    """

    users_list = User.objects.all()

    # if request.method is GET
    return render(
        request,
        "management/management_page.html",
        {
            "users_list": users_list,
        }
    )
