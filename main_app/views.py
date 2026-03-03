from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.views import LoginView
from .models import Garment, Profile
from django.urls import reverse_lazy
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin


class Home(LoginView):
    template_name = 'home.html'

def about(request):
    return render(request, 'about.html')

class ProfileDetail(DetailView):
    model = Profile

class ProfileCreate(CreateView):
    model = Profile
    fields = ['first_name', 'last_name', 'location', 'biography', 'tagline']

class ProfileUpdate(UpdateView):
    model = Profile
    fields = ['first_name', 'last_name', 'location', 'biography', 'tagline']

class GarmentList(LoginRequiredMixin, ListView):
    model = Garment
    fields = '__all_'

    def get_queryset(self):
        return Garment.objects.filter(user=self.request.user)

class GarmentCreate(LoginRequiredMixin, CreateView):
    model = Garment
    fields = ['name', 'story', 'description', 'brand', 'category', 'size', 'condition', 'listing_type']

    def form_valid(self, form):
        form.instance.user = self.request.user 
        return super().form_valid(form)
    
class GarmentDetail(LoginRequiredMixin, DetailView):
    model = Garment

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

class GarmentUpdate(LoginRequiredMixin, UpdateView):
    model = Garment
    fields = ['name', 'story', 'description', 'brand', 'category', 'size', 'condition', 'listing_type']

class GarmentDelete(LoginRequiredMixin, DeleteView):
    model = Garment
    success_url = reverse_lazy('garment-index')

def signup(request):
    error_message = ''
    if request.method == 'POST':
        # This is how to create a 'user' form object
        # that includes the data from the browser
        form = UserCreationForm(request.POST)
        if form.is_valid():
            # This will add the user to the database
            user = form.save()
            # This is how we log a user in
            login(request, user)
            return redirect('garment-index')
        else:
            error_message = 'Invalid sign up - try again'
    # A bad POST or a GET request, so render signup.html with an empty form
    form = UserCreationForm()
    context = {'form': form, 'error_message': error_message}
    return render(request, 'signup.html', context)
    # Same as: 
    # return render(
    #     request, 
    #     'signup.html',
    #     {'form': form, 'error_message': error_message}
    # )
