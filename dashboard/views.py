from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def resident_dashboard(request):
    """
    Display the about page

    **Template:**

    :template:`dashboard/resident_space.html`
    """

    return render(
        request,
        "dashboard/resident_space.html",
    )
