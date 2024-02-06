from django.shortcuts import render,redirect
from django.contrib.auth import login,authenticate,logout
from django.contrib.auth.models import User
from django.contrib import messages # for displaying messages on browser

from .models import Profile # importing Profile model from models.py to get all the Profiles data
# Create your views here.
def loginUser(request): # can't name it login since login is a builtin function from django.contrib.auth
    
    if request.user.is_authenticated: # if user is authenticated don't let them see the login page 
        return redirect('profiles')

    if request.method=="POST":
        #print(request.POST)
        username=request.POST['username']
        password=request.POST['password']

        try:
            user = User.objects.get(username=username)
        except:
            print("Username does not exist")
            messages.error(request,"Username does not exist")
        
        user = authenticate(request,username=username,password=password)

        if user is not None:
            login(request,user)
            return redirect("profiles")
        else:
            messages.error(request,"Username or password is incorrect dumbass")
            
    return render(request,"users/login_register.html")

def logoutUser(request):
    logout(request)
    messages.error(request,"User was successfully logged out")
    return redirect('login')

def profiles(request):
    profiles=Profile.objects.all()
    context={'profiles':profiles}
    return render(request,'users/profiles.html',context) # context needs to be passed here so it can be used in other html templates

def userProfile(request,pk):
    profile= Profile.objects.get(id=pk)
    topSkills = profile.skill_set.exclude(description__exact="") # skill_set is auto created by django to reference kill_set is the manager that allows you to access all the skills related to a specific profile. It provides methods such as all(), filter(), and exclude() for querying the related skills. .exclude with remove those descriptions where the description is empty
    otherSkills= profile.skill_set.filter(description="") # will filter out the skills where description is empty
    context={'profile':profile,'topSkills':topSkills,'otherSkills':otherSkills}
    return render(request,'users/user-profile.html',context)

