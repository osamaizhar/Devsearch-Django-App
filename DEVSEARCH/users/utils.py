# This file shall contain all helper function code, seperating this code for better project management

from .models import Profile,Skill # importing Profile model from models.py to get all the Profiles data
from django.db.models import Q # for complex queries


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
