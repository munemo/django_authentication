from django.shortcuts import render
from my_app.forms import UserForm, UserProfileForm
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required

def index(request):
    return render(request,'my_app/index.html')

@login_required
def user_logout(request):
       logout(request)
       return HttpResponseRedirect(reverse('index'))

def relative(request):
       return render(request, 'my_app/relative.html')

def my_admin(request):
       return render(request,'my_app/my_admin.html')

def signin(request):
       if request.method == 'POST':
              username = request.POST.get('username')
              password = request.POST.get('password')
              
              user = authenticate(username=username,password=password)

              if user:
                     if user.is_active:
                            login(request,user)
                            return HttpResponse(reverse('index'))
                     else:
                            return HttpResponse('Account not active')
              else:
                     print('someone tried to login')
                     print(username,password)
                     return HttpResponse('invalid login')
     
       else:
         return  render(request, 'my_app/signin.html', {})
              

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
       


