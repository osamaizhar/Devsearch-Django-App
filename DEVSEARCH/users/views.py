from django.shortcuts import render
from .models import Profile # importing Profile model from models.py to get all the Profiles data
# Create your views here.
def profiles(request):
    profiles=Profile.objects.all()
    context={'profiles':profiles}
    return render(request,'users/profiles.html',context) # context needs to be passed here so it can be used in other html templates

def userProfile(request,pk):
    profile= Profile.objects.get(id=pk)
    context={'profile':profile}
    return render(request,'users/user-profile.html',context)

