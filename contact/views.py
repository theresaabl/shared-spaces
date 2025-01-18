from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def contact_page(request):
    """
    Display the about page

    **Template:**

    :template:`contact/contact.html`
    """

    return render(
        request,
        "contact/contact.html",
    )
