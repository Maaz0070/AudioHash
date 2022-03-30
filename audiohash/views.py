from django.shortcuts import render
from django.urls import reverse


import requests

# Create your views here.
def index(request):
    return render(request, "audiohash/main.html")
