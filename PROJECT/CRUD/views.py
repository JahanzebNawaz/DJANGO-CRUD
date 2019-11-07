from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UserRegistrationForm
from django.contrib.auth.decorators import login_required

# Create your views here.


def index(request):
    '''
        Index file used to display home page of web app
    '''
    template_url = 'crud/index.html'
    return render(request, template_url)


def register(request):
    '''
        User Registration form, imported UserCreationFrom from auth.form    
    '''
    template_url = 'crud/register.html'
    registration_form = UserRegistrationForm()

    if request.method == 'POST':
        registration_form = UserRegistrationForm(request.POST)
        if registration_form.is_valid():
            registration_form.save()
            username = registration_form.cleaned_data.get('username')
            messages.success(request, f'Successfully account created  {username}!')
            return redirect('login')
        else:
            registration_form = UserRegistrationForm()

    return render(request, template_url, {'form': registration_form})


@login_required(login_url='/login/')
def dashboard(request):
    '''
        Main Home Page after login
    '''
    tempalte_url = 'crud/dashboard.html'
    return render(request, tempalte_url)


@login_required(login_url='/login/')
def profile(request):
    '''
        User Profile Page
    '''
    tempalte_url = 'crud/profile.html'
    return render(request, tempalte_url)