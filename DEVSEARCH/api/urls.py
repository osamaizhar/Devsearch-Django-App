from django.urls import path
from . import views

# -------------- For Json web token -----------------------------------------------------
from rest_framework_simplejwt.views import (
    TokenObtainPairView, # this one will generate the main token    
    TokenRefreshView, # this one will generate refresh token
)

urlpatterns = [
    path('users/token/',TokenObtainPairView.as_view(),name='token_obtain_pair'),
    path('users/token/refresh/',TokenRefreshView.as_view(),name='token_refresh'),
    path('',views.getRoutes),
    path('projects/',views.getProjects),
    path('projects/<str:pk>/',views.getProject)
]