# Create your views here.
from django.shortcuts import render,redirect
from django.http import HttpResponse # used to return a http response 
from .models import Project
from .forms import ProjectForm
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
def createproject(request):
    form = ProjectForm() # creating an object of ProjectForm class in this function
     
    if request.method=="POST":
        #print(request.POST)
        form= ProjectForm(request.POST)
        if form.is_valid(): #.isvalid() method from django with run validation checks on the form
            form.save() # this wil create the form object
            return redirect("projects") # will be redirected to projects url since it matches the name there
    context={"form":form}
    return render(request,"projects/project_form.html",context)

# ************** UPDATE ******************************************************

def updateproject(request,pk): # pk is primary key which will be referencing the id of a project
    project=Project.objects.get(id=pk) # using .get() to fetch project based on id
    form = ProjectForm(instance=project) # instance is the project we want to update
     
    if request.method=="POST":
        #print(request.POST)
        form= ProjectForm(request.POST,instance=project) # instance=project tells which project to update
        if form.is_valid(): #.isvalid() method from django with run validation checks on the form
            form.save() # this wil create the form object
            return redirect("projects") # will be redirected to projects url since it matches the name there
    context={"form":form}
    return render(request,"projects/project_form.html",context)
