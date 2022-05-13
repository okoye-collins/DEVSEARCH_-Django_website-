from django.shortcuts import render
from .models import Profile

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