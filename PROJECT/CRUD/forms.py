from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile

# Create forms here


class UserRegistrationForm(UserCreationForm):
    '''
        User Creation Form
    '''
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class UserUpdateForm(forms.ModelForm):
    '''
        User Update Form
    '''
    email = forms.EmailField()
    
    class Meta:
        model = User
        fields = ['username', 'email']
    

class ProfileUpdateForm(forms.ModelForm):
    '''
        Profile Update Form
    '''    
    class Meta:
        model = Profile
        fields = ['image']