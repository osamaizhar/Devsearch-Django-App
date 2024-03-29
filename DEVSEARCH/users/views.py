from django.shortcuts import render,redirect
from django.contrib.auth import login,authenticate,logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib import messages # for displaying messages on browser
from .models import Profile,Message   # importing Profile model from models.py to get all the Profiles data
#from django.contrib.auth.forms import UserCreationForm # no longer needed since it has been modified in forms.py as CustomUserCreationForm
from .forms import CustomUserCreationForm,ProfileForm,SkillForm,MessageForm 
#from django.db.models import Q # for complex queries
from .utils import searchProfiles,paginateProfiles



def loginUser(request): # can't name it login since login is a builtin function from django.contrib.auth
    page="login"    
    if request.user.is_authenticated: # if user is authenticated don't let them see the login page 
        return redirect('profiles')

    if request.method=="POST":
        #print(request.POST)
        username=request.POST['username'].lower()
        password=request.POST['password']

        try:
            user = User.objects.get(username=username)
        except:
            print("Username does not exist")
            messages.error(request,"Username does not exist")
        
        user = authenticate(request,username=username,password=password)

        if user is not None:
            login(request,user)
            return redirect(request.GET['next'] if 'next' in request.GET else 'account') # sending user to the previous page they were on using get['next'] here
        else:
            messages.error(request,"Username or password is incorrect dumbass")
            
    return render(request,"users/login_register.html")

def logoutUser(request):
    logout(request)
    messages.info(request,"User was successfully logged out")
    return redirect('login')

def registerUser(request):
    page="register"
    form=CustomUserCreationForm() 
    if request.method =="POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user=form.save(commit=False) # temporarily saving form as an object
            user.username= user.username.lower() # lowercasing form username so that 2 same usernames with different casing are not created
            user.save() # now permenantly saving the form
            
            messages.success(request,"User account was successfull created!")   
            login(request,user) # logging in user 
            #return redirect("profiles") # redirecting user to profiles page
            return redirect("edit-account")
        else:
            messages.error(request,"An error occurred during registration")
    context={'page':page,"form":form}
    return render(request,"users/login_register.html",context)

def profiles(request):
    profiles,search_query = searchProfiles(request)
    custom_range,profiles = paginateProfiles(request,profiles,3)
    context={'profiles':profiles,"custom_range":custom_range} # custom_range for pagination
    return render(request,'users/profiles.html',context) # context needs to be passed here so it can be used in other html templates

def userProfile(request,pk):
    profile= Profile.objects.get(id=pk)
    topSkills = profile.skill_set.exclude(description__exact="") # skill_set is auto created by django to reference kill_set is the manager that allows you to access all the skills related to a specific profile. It provides methods such as all(), filter(), and exclude() for querying the related skills. .exclude with remove those descriptions where the description is empty
    otherSkills= profile.skill_set.filter(description="") # will filter out the skills where description is empty
    context={'profile':profile,'topSkills':topSkills,'otherSkills':otherSkills}
    return render(request,'users/user-profile.html',context)


@login_required(login_url='login')
def userAccount(request):
    profile=request.user.profile # getting current logged in user.profile
    skills=profile.skill_set.all()
    projects=profile.project_set.all()
    context={'profile':profile,"skills":skills,"projects":projects}
    return render(request,"users/account.html",context)

@login_required(login_url='login')
def editAccount(request):
    profile=request.user.profile
    form= ProfileForm(instance=profile) # instance=profile allows previous form data to be prefill in fields  Profile Form is a form that allows users to edit their profile information
    if request.method=="POST":
        form=ProfileForm(request.POST,request.FILES,instance=profile)
        if form.is_valid():
            form.save()
            return redirect("account") # redirecting user back to account page once form is updated
    context={"form":form}
    return render(request,'users/profile_form.html',context)


@login_required(login_url='login')
def createSkill(request):
    profile = request.user.profile # getting the owner
    form=SkillForm() # creates instance of form when add skill button is first clicked
    if request.method=="POST": # if submit is clicked it will have POST 
        form= SkillForm(request.POST) # request.POST gets the actual data of form 
        if form.is_valid():
            skill= form.save(commit=False) 
            skill.owner = profile
            skill.save()
            return redirect('account')

    context={'form':form}
    return render(request,"users/skill_form.html",context)


@login_required(login_url='login')
def updateSkill(request,pk):
    profile = request.user.profile # getting the owner
    skill= profile.skill_set.get(id=pk) # getting specific skill via id 
    form=SkillForm(instance=skill) # creates instance of form when update skill button is first clicked
    if request.method=="POST": # if submit is clicked it will have POST 
        form= SkillForm(request.POST,instance=skill) # request.POST gets the actual data of form , setting instance = skill so that form is prefilled with old data 
        if form.is_valid():
            form.save()
            messages.success(request,"Skill was updated successfully")
            return redirect('account')
    context={'form':form}
    return render(request,"users/skill_form.html",context)

def deleteSkill(request,pk):
    profile = request.user.profile
    skill = profile.skill_set.get(id=pk)
    if request.method=="POST":
        skill.delete()
        messages.success(request,"Skill was Deleted Successfully!")
        return redirect('account')
    context = {'object':skill}
    return render(request,'delete_template.html',context)
  
@login_required(login_url="login")
def inbox(request):
    profile = request.user.profile
    messageRequests = profile.messages.all() # accessing related_name messages here to get all messages for the profile
    unreadCount = messageRequests.filter(is_read=False).count() 
    context={"messageRequests":messageRequests,"unreadCount":unreadCount}
    print("MESSAGE REQUESTS: ",messageRequests)
    return render(request,'users/inbox.html',context)
    
@login_required(login_url='login')
def viewMessage(request,pk):
    profile = request.user.profile
    message = profile.messages.get(id=pk)
    # adding functionality to make the message read
    if message.is_read == False:
        message.is_read = True 
        message.save()
    context = {'message': message}
    return render(request,'users/message.html',context)

def createMessage(request,pk):
    recipient = Profile.objects.get(id=pk)
    form = MessageForm()
    # we can also test if user is authenticated instead of this
    try:
        sender = request.user.profile
    except:
        sender = None

    if request.method == "POST":
        form = MessageForm(request.POST)
        if form.is_valid():
            message = form.save(commit=False) 
            message.sender = sender
            message.recipient = recipient

            if sender: # if theere is a sender then that means user is logged in and we can get these details
                message.name = sender.name
                message.email = sender.email
            print("RECIPIENT AND THE MESSAGE:",recipient,message)

            message.save()

            messages.success(request,"Your message was Successfully sent!")
            return redirect('user-profile',pk=recipient.id)
 
    context = {'recipient':recipient,'form':form}
    return render(request,'users/message_form.html',context)
    