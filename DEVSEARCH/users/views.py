from django.shortcuts import render
from .models import Profile # importing Profile model from models.py to get all the Profiles data
# Create your views here.
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

