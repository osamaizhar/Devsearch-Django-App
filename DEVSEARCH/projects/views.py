# Create your views here.
from django.shortcuts import render,redirect
from django.http import HttpResponse # used to return a http response 
from .models import Project
from .forms import ProjectForm
from django.contrib.auth.decorators import login_required

# projectList here is global no longer using it since data is being fetched from db

# projectsList = [

# {'id': '1', 'title': 'Ecommerce Website', 'description': 'Fully functional ecommerce website' },
# { 'id': '2', 'title': 'Portfolio Website', 'description': 'A personal website to write articles and display work' },
# {'id': '3', 'title': 'Social Network', 'description': 'An open source project built by the community' }

# ]

def projects(request):
    # return HttpResponse("Here are our projects")
    projects=Project.objects.all()
    context={"projects":projects}
    return render(request,"projects/projects.html",context) # rendering view from html template using render


def project(request,pk):
    #return HttpResponse("Here are our projects "+pk)
    projectObj= Project.objects.get(id=pk)
    return render(request,"projects/single-project.html",{'project':projectObj}) # we added projects/ because we have made a 
    # new file structure so that all templates related to projects app are inside the projects app as
    # projects/templates/projects
    # root template folder will only have general templates
    
# *************** CRUD OPS ***********************************************************

# ************** CREATE ******************************************************
@login_required(login_url="login") # login_url is where the user should be redirected if the user is not logged in
def createproject(request):
    profile = request.user.profile
    form = ProjectForm() # creating an object of ProjectForm class in this function
     
    if request.method=="POST":
        #print(request.POST)
        form= ProjectForm(request.POST,request.FILES) # request.FILES will access the files from the request as well
        if form.is_valid(): #.isvalid() method from django with run validation checks on the form
            project= form.save(commit=False) # this wil create the form object
            project.owner = profile # doing this to show the name of user on their project apparently
            project.save()
            return redirect("account") # will be redirected to projects url since it matches the name there
    context={"form":form}
    return render(request,"projects/project_form.html",context)

# ************** UPDATE ******************************************************
@login_required(login_url="login")
def updateproject(request,pk): # pk is primary key which will be referencing the id of a project'
    profile = request.user.profile # getting current logged user via the one to one relationship
    
    #project=Project.objects.get(id=pk) # using .get() to fetch project based on id (old way)
    project = profile.project_set.get(id=pk) # this is now going to get all the child project (project_set) from the currently logged user via profile

    form = ProjectForm(instance=project) # instance is the project we want to update
     
    if request.method=="POST":
        #print(request.POST)
        form= ProjectForm(request.POST,request.FILES,instance=project) # instance=project tells which project to update
        if form.is_valid(): #.isvalid() method from django with run validation checks on the form
            form.save() # this wil create the form object
            return redirect("account") # will be redirected to account url since it matches the name there
    context={"form":form}
    return render(request,"projects/project_form.html",context)

# ************** DELETE ******************************************************
@login_required(login_url="login")
def deleteproject(request,pk):
    profile = request.user.profile 
    #project = Project.objects.get(id=pk)
    project=profile.project_set.get(id=pk)
    if request.method == "POST":
        project.delete()
        return redirect('projects')
    context = {"object":project}
    return render(request,"delete_template.html",context)