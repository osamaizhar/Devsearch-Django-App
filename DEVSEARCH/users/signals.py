
# ---------------------------- Signal-related imports ----------------------------------------------------    

from django.db.models.signals import post_save,post_delete 
from django.dispatch import receiver

# ------------------------ Email Functionality Related imports -----------------------------------
from django.core.mail import send_mail
from django.conf import settings

# ---------------------------- Model Imports ----------------------------------------------------    

from django.contrib.auth.models import User
from .models import Profile

# ---------------------------- Creating Signal ----------------------------------------------------    

#@receiver(post_save,sender=Profile) # connecting signal via decorator
def createProfile(sender,instance,created,**kwargs): # sender is the model that triggers it, instance is object of model that triggered,created is boolean if model was added or saved again
    print("Profile Saved!")
    # print("Instance:",instance,type(instance))
    # print("Created:",created,type(created))
    if created: # whenever a new user is created/added to User
        user=instance
        profile=Profile.objects.create(
            user=user,
            username=user.username,
            email=user.email,
            name=user.first_name
        )
        # ---- For sending Registration Completed Successfully Email ------------------------------
        
        subject = "Welcome to DevSearch"
        message = "We are glad you are here!"
        
        send_mail(
            subject,
            message,
            settings.EMAIL_HOST_USER,
            [profile.email],
            fail_silently=False
        )
        

# this signal is required to update the User Model as soon as Profile Model is updated since Profile Model is acting as User model
def updateUser(sender,instance, created,**kwargs):
    profile=instance # since it is a one to one relationship between profile and user we can get user form profile via profile.user
    user = profile.user 
    if created==False: # checking if it's not the first time profile is created, if we don't do this step then user.save() will call createProfile and both will be stuck in infinite loop leading to recursion error
        user.first_name=profile.name
        user.username=profile.username
        user.email=profile.email
        user.save()


def deleteUser(sender,instance,**kwargs): # it will delete the user if the profile is also deleted
    user=instance.user
    print("Instance:",instance,type(instance))
    print("user:",user,type(user)) 

    user.delete()
    print(f"Deleting the User {instance.username} ...")


# ---------------------------- Connecting Signal without decorators---------------------------------------------------- 
post_delete.connect(deleteUser,sender=Profile) # anytime a user is created it will trigger
post_save.connect(createProfile,sender=User) # signal is connect with Profile model via sender param
post_save.connect(updateUser,sender=Profile) 