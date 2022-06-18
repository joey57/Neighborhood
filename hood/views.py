from cmath import log
from django.shortcuts import render, redirect, get_object_or_404
from django.http  import HttpResponse, Http404, HttpResponseRedirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .forms import UserRegisterForm, UpdateProfileForm, NeighbourHoodForm, BusinessForm, PostForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .models import Profile, NeighbourHood, Business, Post

# Create your views here.
def index(request):
  return render(request, 'index.html')

def hoods(request):
  all_hoods = NeighbourHood.objects.all()
  all_hoods = all_hoods[::-1]
  params = {
    'all_hoods': all_hoods,
  }
  return render(request, 'all_hoods.html', params)

def create_hood(request):
  if request.method == 'POST':
    form = NeighbourHoodForm(request.POST, request.FILES)
    if form.is_valid():
       hood = form.save(commit=False)
       hood.admin = request.user.profile
       hood.save()
       return redirect('hood')
  else:
    form = NeighbourHoodForm()
  return render(request, 'newhood.html', {'form': form})

def single_hood(request, hood_id):
  hood = NeighbourHood.objects.get(id=hood_id)
  business = Business.objects.filter(neighbourhood=hood)
  posts = Post.objects.filter(hood=hood)
  posts = posts[::-1]
  if request.method == 'POST':
    form = BusinessForm(request.POST)
    if form.is_valid():
      biz_form = form.save(commit=False)
      biz_form.neighbourhood = hood
      biz_form.user = request.user.profile
      biz_form.save()
      return redirect('single-hood', hood.id)
  else:
    form = BusinessForm()
  params = {
    'hood': hood,
    'business': business,
    'form': form,
    'posts': posts
  }
  return render(request, 'single_hood.html', params)

@login_required
def join_hood(request, id):
    neighbourhood = get_object_or_404(NeighbourHood, id=id)
    request.user.profile.neighbourhood = neighbourhood
    request.user.profile.save()
    return redirect('hood')

def leave_hood(request, id):
    hood = get_object_or_404(NeighbourHood, id=id)
    request.user.profile.neighbourhood = None
    request.user.profile.save()
    return redirect('hood')


def search_business(request):
  if request.method == 'GET':
    name = request.GET.get("title")
    results = Business.objects.filter(name__icontains=name).all()
    print(results)
    message = f'name'
    params = {
      'results': results,
      'message': message
    }
    return render(request, 'search_results.html', params)
  else:
    message = "You haven't searched for any business"
  return render(request, "search_results.html")

def create_post(request, hood_id):
  hood = NeighbourHood.objects.get(id=hood_id)
  if request.method == 'POST':
    form = PostForm(request.POST)
    if form.is_valid():
      post = form.save(commit=False)
      post.hood = hood
      post.user = request.user.profile
      post.save()
      return redirect('single-hood', hood.id)
  else:
    form = PostForm()
  return render(request, 'post.html', {'form': form})


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
  