from cmath import log
from django.shortcuts import render, redirect
from django.http  import HttpResponse, Http404, HttpResponseRedirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .forms import UserRegisterForm, UpdateProfileForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

# Create your views here.
def index(request):
  return render(request, 'index.html')
  


def register(request):
  if request.method == 'POST':
    form = UserRegisterForm(request.POST)
    if form.is_valid():
      form.save()
      username = form.cleaned_data.get('username')
      messages.success(request, f'Your account has been created you are now able to login {username}')
      return redirect('login')
  else:
    form = UserRegisterForm()
  return render(request, 'users/register.html',{"form":form})

@login_required
def profile(request, username):
  return render(request, 'users/profile.html')

@login_required
def update_profile(request,username):
  user=User.objects.get(username=username)
  current_user = request.user
  
  if request.method =='POST':
    form = UpdateProfileForm(request.POST,request.FILES, instance=current_user.profile)
    
    if form.is_valid():
      form.save()
      return redirect('profile', user.username)
  
  else:
    form = UpdateProfileForm(instance=current_user.profile)
  return render(request,"users/update_profile.html", {"form":form})
  