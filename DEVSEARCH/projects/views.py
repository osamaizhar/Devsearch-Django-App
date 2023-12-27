from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse # used to return a http response 

# projectList here is global
projectsList = [

{'id': '1', 'title': 'Ecommerce Website', 'description': 'Fully functional ecommerce website' },
{ 'id': '2', 'title': 'Portfolio Website', 'description': 'A personal website to write articles and display work' },
{'id': '3', 'title': 'Social Network', 'description': 'An open source project built by the community' }

]

def projects(request):
    # return HttpResponse("Here are our projects")
    page="projects"
    number=11
    context={"page":page,"number":number,"projects":projectsList}
    return render(request,"projects/projects.html",context) # rendering view from html template using render


def project(request,pk):
    #return HttpResponse("Here are our projects "+pk)
    projectObj=None
    for i in projectsList:
        if i["id"]==pk:
            projectObj=i
    return render(request,"projects/single-project.html",{'project':projectObj}) # we added projects/ because we have made a 
    # new file structure so that all templates related to projects app are inside the projects app as
    # projects/templates/projects
    # root template folder will only have general templates
    
