from .models import Project, Tag
from django.db.models import Q
from django.core.paginator import Paginator,PageNotAnInteger,EmptyPage

def paginateProjects(request,projects,results):
    page=request.GET.get('page')

    paginator=Paginator(projects,results)
    #projects= paginator.page(page)
    
    try:
        projects= paginator.page(page)
    except PageNotAnInteger: # this will error from when we first arrive on the page 
        page=1
        projects = paginator.page(page)
    except EmptyPage: # this will fix error for if the user goes to a page that does not exist
        page=paginator.num_pages # getting the number of pages which should also be the num of the last page
        projects = paginator.page(page)   # showing last page

    # ------------- Creating Custom Index to resolve infinite pagination numbers jugari sol by dennis -----------------------
    
    #custom_range=range(1,2000) # for testing unlimited pagination
    leftIndex = int(page)-3
    if leftIndex < 1:
        leftIndex = 1
    rightIndex = int(page)+2
    if rightIndex > paginator.num_pages: # if the right index value exceeds the max number of pages then it will be reset to max number of pages 
        rightIndex = paginator.num_pages
    custom_range = range(leftIndex,rightIndex+1) # this will show only limited pagination numbers
    print("Projects:",projects)       
    print("paginator result:" ,paginator)
 
    return custom_range,projects


def searchProjects(request):
    
    search_query = ""
    if request.GET.get('search_query'):
        search_query = request.GET.get('search_query')
    
    tags= Tag.objects.filter(name__icontains=search_query)
    projects = Project.objects.distinct().filter(
        Q(title__icontains=search_query) |
        Q(description__icontains=search_query) |
        Q(owner__name__icontains=search_query) |
        Q(tags__in=tags)
    )                        
    return projects, search_query

