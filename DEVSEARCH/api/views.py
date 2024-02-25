#from django.http import JsonResponse | replaced by django rest framework
from rest_framework.decorators import api_view,permission_classes # basically controls what REST methods can the view handle
from rest_framework.permissions import IsAuthenticated,IsAdminUser
from rest_framework.response import Response # creates http responses 
from .serializers import ProjectSerializer # converts complex data into format that can be easily rendered into json 
from projects.models import Project

@api_view(['GET'])
def getRoutes(request):

    routes= [
        {'GET':'/api/projects'},
        {'GET':'/api/projects/id'},
        {'POST':'/api/projects/id/vote'},
        {'POST':'/api/users/token'},
        {'POST':'/api/users/token/refresh'},
    ]

    #return JsonResponse(routes,safe=False) # for safe info look into api notes , return more than python dict
    return Response(routes) # using django restframework for response

@api_view(["GET"]) 
#@permission_classes([IsAuthenticated])
def getProjects(request):
    print('USER:',request.user)
    projects = Project.objects.all() 
    serializer = ProjectSerializer(projects,many=True) # many is set to true here since we will be returning many objects
    return Response(serializer.data)
# ------------------ For Single Project -----------------------------------------
@api_view(["GET"])
def getProject(request,pk):
    project = Project.objects.get(id=pk) 
    serializer = ProjectSerializer(project,many=False) # many is set to true here since we will be returning many objects
    return Response(serializer.data)