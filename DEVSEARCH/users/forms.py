from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Profile,Skill,Message

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model=User
        fields=['first_name','email','username','password1','password2']
        labels ={ # we can modify the form fields using labels
            "first_name":"Name"
        }
        
# Modifying the customusercreation form by adding input class to each field so that the theme input class can apply styling to those fields did the same thing for projects app forms.py
    def __init__(self,*args,**kwargs):
        super(CustomUserCreationForm,self).__init__(*args,**kwargs)

        for name,field in self.fields.items():
            field.widget.attrs.update({'class':'input'}) 

class ProfileForm(ModelForm):
    class Meta:
        model= Profile
        #fields="__all__"
        exclude = {'user'}  # will basically exclude user and show all fields 
    
    def __init__(self,*args,**kwargs):
        super(ProfileForm,self).__init__(*args,**kwargs)

        for name,field in self.fields.items():
            field.widget.attrs.update({'class':'input'}) 

class SkillForm(ModelForm):
    class Meta:
        model=Skill
        fields= "__all__"
        exclude=['owner']

    def __init__(self,*args,**kwargs):
        super(SkillForm,self).__init__(*args,**kwargs)

        for name,field in self.fields.items():
            field.widget.attrs.update({'class':'input'})

class MessageForm(ModelForm):
    class Meta:
        model=Message
        fields= ['name','email','subject','body']

    def __init__(self,*args,**kwargs):
        super(MessageForm,self).__init__(*args,**kwargs)

        for name,field in self.fields.items():
            field.widget.attrs.update({'class':'input'})

