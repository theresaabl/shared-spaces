from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def resident_dashboard(request):
    return HttpResponse("This is your resident dashboard.")
