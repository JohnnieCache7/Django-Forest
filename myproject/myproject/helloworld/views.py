from django.shortcuts import render
from django.http import HttpResponse


def home(request):
    return HttpResponse("Hello, World! from Jonathan Argueta-Herrera on 3/24/2024")


# Create your views here.
