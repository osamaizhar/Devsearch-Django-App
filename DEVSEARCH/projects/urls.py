from django.urls import path
from . import views  # . means same file path , importing views here so we can use those functions with these urls
# Putting all urls related to projects here to organize code better

urlpatterns = [
    path("",views.projects,name="projects"),
    path("project/<str:pk>/",views.project,name="project"),
    path("create-project/",views.createproject,name="create-project"),
    path("update-project/<str:pk>",views.updateproject,name="update-project"),
    path("delete-project/<str:pk>",views.deleteproject,name="delete-project"),
    
]
 