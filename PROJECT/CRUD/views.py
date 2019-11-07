from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UserRegistrationForm, UserUpdateForm, ProfileUpdateForm
from django.contrib.auth.decorators import login_required
from .models import Courses
from django.http import HttpResponse

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
        try:
            registration_form = UserRegistrationForm(request.POST)
        except UserRegistrationForm.DoesNotExist():
            return HttpResponse('Error getting form')
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
    try:
        courses = Courses.objects.all()
    except Courses.DoesNotExist():
        return HttpResponse("No Such Model found.")

    return render(request, tempalte_url, {'courses': courses})


@login_required(login_url='/login/')
def profile(request):
    '''
        User Profile Page
    '''
    if request.method == 'POST':
        try:
            user_form = UserUpdateForm(request.POST, instance=request.user)
            profile_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)
        except UserUpdateForm.DoesNotExist() or ProfileUpdateForm.DoesNotExist():
            return HttpResponse('Error getting forms')

        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()

            messages.success(request, f'Your details has been updated')
            return redirect('profile')
    else:
        user_form = UserUpdateForm(instance=request.user)
        profile_form = ProfileUpdateForm(instance=request.user.profile)

    context = {
        'user_form': user_form,
        'profile_form': profile_form
    }
    tempalte_url = 'crud/profile.html'
    return render(request, tempalte_url, context)



