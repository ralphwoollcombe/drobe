from django.shortcuts import render
from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView
from .models import Garment

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

class GarmentList(ListView):
    model = Garment
    fields = '__all_'

class GarmentCreate(CreateView):
    model = Garment
    fields = '__all_'