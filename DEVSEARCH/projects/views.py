from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse # used to return a http response 

def projects(request):
    # return HttpResponse("Here are our projects")
    return render(request,"projects.html") # rendering view from html template using render
def project(request,pk):
    #return HttpResponse("Here are our projects "+pk)
    return render(request,"single-project.html")
    
