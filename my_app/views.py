from django.shortcuts import render
from django.contrib.auth import authenticate

from my_app.forms import UserForm, UserProfileForm

def index(request):
    return render(request,'my_app/index.html')

def relative(request):
       return render(request, 'my_app/relative.html')

def my_admin(request):
       return render(request,'my_app/my_admin.html')

def signin(request):
       
       return render(request,'my_app/signin.html')

def other(request):
       return render(request,'my_app/other.html')


def  register(request):
       
       registered = False
       
       if request.method == 'POST':
                            
              user_form = UserForm(data=request.POST)
              profile_form = UserProfileForm(data=request.POST)
              
              if user_form.is_valid() and profile_form.is_valid():
                     user = user_form.save()
                     user.set_password(user.password)
                     user.save()
                     
                     profile = profile_form.save(commit=False)
                     profile.user = user
                     
                     if 'profile_pic' in request.FILES:
                            profile.profile_pic = request.FILES['profile_pic']
                            
                            profile.save()
                            
                            registered = True
              else:
                     print(user_form.errors, profile_form.errors)
       else:
              user_form = UserForm
              profile_form = UserProfileForm()
       return render(request, 'my_app/registration.html', 
                     {'user_form':user_form,'profile_form':profile_form,'registered':registered})     
       


