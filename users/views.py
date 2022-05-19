from multiprocessing import context
from django.shortcuts import redirect, render
from .models import Profile
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.models import User
from django.contrib import messages
from .forms import customUserCreationForm

# Create your views here.

def profile(request):
    profiles = Profile.objects.all()
    context = {'profiles':profiles}
    return render(request, 'users/profiles.html', context)

def userprofile(request, pk):
    profile = Profile.objects.get(id=pk)
    top_skill = profile.skill_set.exclude(description__exact = "")
    other_skill = profile.skill_set.filter(description="")
    context = {
        'profile': profile,
        'top_skill':top_skill,
        'other_skill':other_skill,
    }
    return render(request, 'users/user-profile.html', context)

def loginUser(request):
    page= 'login'

    if request.user.is_authenticated:
        return redirect('project:index')

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        # print(request.POST)
        try:
            user =  User.objects.get(username=username)
        except:
            # print('username does not exist')
            messages.error(request, 'username does not exist')
        
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)
            return redirect('project:index')
        else:
            messages.error(request, 'Username or Password is incorrect')

    return render(request, 'users/login_register.html')

def logoutUser(request):
    logout(request)
    messages.success(request, 'User was successfully logout')
    return redirect('users:login')

def registerUser(request):
    page= 'signup'
    form = customUserCreationForm
    if request.method == 'POST':
        form = customUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()
            messages.success(request, f'{user.username} account was created! ')

            login(request, user)
            return redirect('users:profile')

        else:
            messages.success(request, 'An error has occurred during regisrations!')

           
    context = {
        'page': page,
        'form':form,
        }
    return render(request, 'users/login_register.html', context)