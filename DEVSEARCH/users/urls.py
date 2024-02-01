from django.urls import path
from . import views # using . means you are importing from same dir

urlpatterns = [
    path('',views.profiles,name='profiles'),
    path("profile/<str:pk>",views.userProfile,name="user-profile")
]