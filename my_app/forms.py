from django.contrib.auth.models import User
from my_app.models import UserProfileInfo
from django import forms
from django.forms import fields


class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    
    class Meta():
            model = User
            fields = ["username", "email", "password"]
        
class UserProfileForm(forms.ModelForm):
    class Meta():
        model = UserProfileInfo
        fields = ["portfolio_site", "profile_pic"]
        
class SignInForm(forms.ModelForm):
    class Meta():
            model = User
            fields = ["username", "password"]