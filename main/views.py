from django.shortcuts import render
from django.http import HttpResponseRedirect


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
    Display the about section

    **Template:**

    :template:`main/index.html`
    """

    return HttpResponseRedirect('/#about-section')
