
# ---------------------------- Signal-related imports ----------------------------------------------------    

from django.db.models.signals import post_save,post_delete 
from django.dispatch import receiver

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

def deleteUser(sender,instance,**kwargs): # it will delete the user if the profile is also deleted
    user=instance.user
    print("Instance:",instance,type(instance))
    print("user:",user,type(user)) 

    user.delete()
    print(f"Deleting the User {instance.username} ...")


# ---------------------------- Connecting Signal without decorators---------------------------------------------------- 
post_delete.connect(deleteUser,sender=Profile) # anytime a user is created it will trigger
post_save.connect(createProfile,sender=User) # signal is connect with Profile model via sender param
