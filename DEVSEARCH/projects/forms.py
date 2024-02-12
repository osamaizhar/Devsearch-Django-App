from django.forms import ModelForm,widgets
from django import forms
from .models import Project # importing model (from class Project)

class ProjectForm(ModelForm): # this will be form for Project model"
    class Meta:
        model = Project
        #fields = "__all__" # __all__ will add all the editable fields to form , 
        # if we want to specify fields then we can give a list
        fields=["title","featured_image","description","demo_link","source_link","tags"]
        widgets={
            "tags":forms.CheckboxSelectMultiple() # to change the list of tags into check boxes
        }
        
    def __init__(self,*args,**kwargs):
        super(ProjectForm,self).__init__(*args,**kwargs)
        for name,field in self.fields.items():
            field.widget.attrs.update({'class':'input'}) # adding fronted theme class input here into django widget
        #self.fields['title'].widget.attrs.update({"class":'input'})
        

