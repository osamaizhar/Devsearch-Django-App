from django.forms import ModelForm
from .models import Project # importing model (from class Project)

class ProjectForm(ModelForm): # this will be form for Project model
    class Meta:
        model = Project
        #fields = "__all__" # __all__ will add all the editable fields to form , if we want to specify fields then we can give a list
        fields=["title","featured_image","description","demo_link","source_link","tags"]
        a=0
        
    
