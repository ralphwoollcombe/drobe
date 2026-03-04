from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.views import LoginView
from .models import Garment, Profile, Community, Transaction
from .forms import TransactionForm
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
    fields = ['first_name', 'last_name', 'location', 'biography', 'tagline', 'image']

class GarmentList(LoginRequiredMixin, ListView):
    model = Garment
    fields = '__all_'

    def get_queryset(self):
        return Garment.objects.filter(user=self.request.user)

class GarmentCreate(LoginRequiredMixin, CreateView):
    model = Garment
    fields = ['name', 'story', 'description', 'brand', 'category', 'size', 'condition', 'listing_type', 'image']

    def form_valid(self, form):
        form.instance.user = self.request.user 
        return super().form_valid(form)
    
class GarmentDetail(LoginRequiredMixin, DetailView):
    model = Garment

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['transaction_form'] = TransactionForm()
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
    fields = ['name', 'description', 'location', 'style_focus', 'image']

    def form_valid(self, form):
        form.instance.created_by = self.request.user 
        response = super().form_valid(form)
        self.object.members.add(self.request.user)
        return response
    
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

class TransactionList(ListView):
    model = Transaction

    def get_queryset(self):
        user = self.request.user
        direction = self.request.GET.get('direction')
        transaction_type = self.request.GET.get('type')

        if direction == 'outgoing':
            queryset = Transaction.objects.filter(from_user=user)
        elif direction == 'incoming':
            queryset = Transaction.objects.filter(to_user=user)
        else:
            return Transaction.objects.none()
        
        if transaction_type:
            queryset = queryset.filter(transaction_type=transaction_type)
    
        return queryset.order_by('-created_at')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['direction'] = self.request.GET.get('direction', '')
        context['type'] = self.request.GET.get('type', '')
        context['pending_outgoing'] = Transaction.objects.filter(
            from_user=self.request.user,
            status='pending'
        ).order_by('-created_at')
        context['pending_incoming'] = Transaction.objects.filter(
            to_user=self.request.user,
            status='pending'
        ).order_by('-created_at')
        return context

@login_required
def initiate_transaction(request, pk):
    garment = Garment.objects.get(id=pk)
    
    if garment.status != 'available':
        return redirect('garment-detail', pk=pk)
    
    if 'borrow' in request.POST:
        transaction_type = 'lend'
    elif 'adopt' in request.POST:
        transaction_type = 'gift'
    else:
        return redirect('garment-detail', pk=pk)
    
    form = TransactionForm(request.POST)
    if form.is_valid():
        new_transaction = form.save(commit=False)
        new_transaction.garment = garment
        new_transaction.from_user = garment.user
        new_transaction.to_user = request.user
        new_transaction.transaction_type = transaction_type
        new_transaction.status = 'pending'
        new_transaction.points_exchanged = garment.points_value
        new_transaction.save()

        garment.status = 'pending'
        garment.save()

    return redirect('garment-detail', pk=pk)

@login_required
def approve_transaction(request, pk):
    transaction = Transaction.objects.get(id=pk)

    if transaction.from_user != request.user:
        return redirect('garment-detail', pk=transaction.garment.id)

    garment = transaction.garment

    if transaction.transaction_type == 'gift':
        garment.user = transaction.to_user
        garment.status = 'gifted'
        garment.save()

        transaction.status = 'gifted'
        transaction.save()

        giver_profile = transaction.from_user.profile
        receiver_profile = transaction.to_user.profile
        giver_profile.points += transaction.points_exchanged
        giver_profile.save()
        receiver_profile.points -= transaction.points_exchanged
        receiver_profile.save()

    elif transaction.transaction_type == 'lend':
        garment.status = 'borrowed'
        garment.save()

        transaction.status = 'borrowed'
        transaction.save()

        lender_profile = transaction.from_user.profile
        borrower_profile = transaction.to_user.profile
        lender_profile.points += transaction.points_exchanged
        lender_profile.save()
        borrower_profile.points -= transaction.points_exchanged
        borrower_profile.save()

    return redirect('garment-detail', pk=garment.id)

@login_required
def decline_transaction(request, pk):
    transaction = Transaction.objects.get(id=pk)

    if transaction.from_user != request.user:
        return redirect('garment-detail', pk=transaction.garment.id)

    garment = transaction.garment
    garment.status = 'available'
    garment.save()

    transaction.delete()

    return redirect('garment-detail', pk=garment.id)
   
@login_required
def associate_member(request, user_id, community_id):
    Community.objects.get(id=community_id).members.add(user_id)
    return redirect('community-detail', pk=community_id)

@login_required
def remove_member(request, user_id, community_id):
    Community.objects.get(id=community_id).members.remove(user_id)
    return redirect('community-detail', pk=community_id)

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
