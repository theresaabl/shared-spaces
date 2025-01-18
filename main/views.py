from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def home_page(request):
    """
    Display the homepage

    **Template:**

    :template:`main/index.html`
    """

    return render(
        request,
        "main/index.html",
    )


def about_page(request):
    """
    Display the about page

    **Template:**

    :template:`main/about.html`
    """

    return render(
        request,
        "main/about.html",
    )
