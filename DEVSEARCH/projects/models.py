from django.db import models
import uuid
# Create your models here.

class Project(models.Model):
    title= models.CharField(max_length=200)
    description= models.TextField(null=True,blank=True)
    featured_image= models.ImageField(null=True,blank=True,default="default.jpg") # requires pillow to use
    demo_link= models.CharField(max_length=2000,null=True,blank=True)
    source_link= models.CharField(max_length=2000,null=True,blank=True)
    tags= models.ManyToManyField("Tag", blank=True) # using Tag as string since it is referenced afterwards so python will be able to find it
    vote_total= models.IntegerField(default=0,null=True,blank=True)
    vote_ratio= models.IntegerField(default=0,null=True,blank=True)
    created= models.DateTimeField(auto_now_add=True) # auto_now_add adds timestamp automatically as model instance is created
    id= models.UUIDField(default=uuid.uuid4,unique=True,primary_key=True,editable=False) # UUID 16 character unique ids
                                    # uuid4 is encoding type              # so no one can edit it
    def __str__(self):
        return self.title
    
class Review(models.Model):
    VOTE_TYPE =(
        ('up',"Up Vote"), # first one is reference , second one is display output    
        ('down',"Down Vote")
    )
                                                    # if SET_NULL was used here then when project is delted this project field will be set to null 
                                                    # Cascade will delete all the reviews if the project is deletedf
    project= models.ForeignKey(Project, on_delete=models.CASCADE)
    body= models.TextField(null=True,blank=True)
    value= models.CharField(max_length=200, choices=VOTE_TYPE)
    created= models.DateTimeField(auto_now_add=True) # auto_now_add adds timestamp automatically as model instance is created
    id= models.UUIDField(default=uuid.uuid4,unique=True,primary_key=True,editable=False)


    def __str__(self):
        return self.value

class Tag(models.Model):
    name= models.CharField(max_length=200)
    created= models.DateTimeField(auto_now_add=True)
    id= models.UUIDField(default=uuid.uuid4, unique=True,
                        primary_key=True,editable=False)

    def __str__(self):
        return self.name 