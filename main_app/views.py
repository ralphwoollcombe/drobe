from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.views import LoginView
from .models import Garment, Profile, Community
from django.urls import reverse_lazy
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin


class Home(LoginView):
    template_name = 'home.html'

def about(request):
    return render(request, 'about.html')

class MyProfile(DetailView):
    model = Profile
    template_name = 'main_app/profile_detail.html'
    context_object_name = 'profile'

    def get_object(self):
        return self.request.user.profile
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['garment_list'] = Garment.objects.filter(user=self.request.user)
        return context

class ProfileDetail(DetailView):
    model = Profile

    def get_object(self):
        return Profile.objects.get(user__id=self.kwargs['pk'])
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['garment_list'] = Garment.objects.filter(user=self.object.user)
        return context
    
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

class CommunityList(LoginRequiredMixin, ListView):
    model = Community
    fields = '__all_'

    def get_queryset(self):
        return Community.objects.filter(members=self.request.user)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        other_communities = Community.objects.exclude(members=self.request.user).order_by('?')
        context['other_communities'] = other_communities[:6]
        return context

class CommunityCreate(LoginRequiredMixin, CreateView):
    model = Community
    fields = ['name', 'description', 'location', 'style_focus']

    # def form_valid(self, form):
    #     form.instance.user = self.request.user 
    #     return super().form_valid(form)
    
class CommunityDetail(LoginRequiredMixin, DetailView):
    model = Community

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     return context

class CommunityUpdate(LoginRequiredMixin, UpdateView):
    model = Community
    fields = ['name', 'description', 'location', 'style_focus']

class CommunityDelete(LoginRequiredMixin, DeleteView):
    model = Community
    success_url = reverse_lazy('community-index')


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
