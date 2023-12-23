from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse # used to return a http response 

def projects(request):
    # return HttpResponse("Here are our projects")
    msg="Helo, you are on Projects Page!"
    return render(request,"projects/projects.html",{"message":msg}) # rendering view from html template using render
def project(request,pk):
    #return HttpResponse("Here are our projects "+pk)
    return render(request,"projects/single-project.html") # we added projects/ because we have made a 
    # new file structure so that all templates related to projects app are inside the projects app as
    # projects/templates/projects
    # root template folder will only have general templates
    
