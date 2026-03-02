from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Garment

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

class GarmentList(ListView):
    model = Garment

