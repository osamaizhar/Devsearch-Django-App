# This file shall contain all helper function code, seperating this code for better project management

from .models import Profile,Skill # importing Profile model from models.py to get all the Profiles data
from django.db.models import Q # for complex queries
from django.core.paginator import Paginator,PageNotAnInteger,EmptyPage

def paginateProfiles(request,profiles,results):
    page=request.GET.get('page')
    paginator=Paginator(profiles,results)
    
    try:
        profiles= paginator.page(page)
    except PageNotAnInteger: # this will error from when we first arrive on the page 
        page=1
        profiles = paginator.page(page)
    except EmptyPage: # this will fix error for if the user goes to a page that does not exist
        page=paginator.num_pages # getting the number of pages which should also be the num of the last page
        profiles = paginator.page(page)   # showing last page

    # ------------- Creating Custom Index to resolve infinite pagination numbers jugari sol by dennis -----------------------
    
    #custom_range=range(1,2000) # for testing unlimited pagination
    leftIndex = int(page)-3
    if leftIndex < 1:
        leftIndex = 1
    rightIndex = int(page)+2
    if rightIndex > paginator.num_pages: # if the right index value exceeds the max number of pages then it will be reset to max number of pages 
        rightIndex = paginator.num_pages
    custom_range = range(leftIndex,rightIndex+1) # this will show only limited pagination numbers
    print("profiles:",profiles)       
    print("paginator result:" ,paginator)
 
    return custom_range,profiles

def searchProfiles(request):
    search_query = ''

    if request.GET.get('search_query'):
        search_query = request.GET.get('search_query')
    print(f"request: {request} GET: {request.GET} .get: {request.GET.get('search_query')} ")
    print("SEARCH:",search_query)
    # ---------------------- Creating Search query based on skill ---------------------------------------------------
    skills = Skill.objects.filter(name__icontains=search_query)
    #profiles=Profile.objects.all() # old code
    # --------- Creating Search Query based on name and short intro containing one of the search item ---------------------
    profiles= Profile.objects.distinct().filter(Q(name__icontains=search_query) |  # adding distinct to avoid duplication issue due to skill__in
    Q(short_intro__icontains = search_query) |
    
    Q(skill__in=skills) # check if skill in skill list, however this creates issue where you see duplicates even before searching because there are multiple skills

    ) # icontains will basically make it not case sensitve
    return profiles,search_query

