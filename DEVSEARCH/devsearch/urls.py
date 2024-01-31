"""
URL configuration for devsearch project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path , include

from django.conf import settings # gives access to settings.py file
from django.conf.urls.static import static

# Moved all urls to urls.py inside of projects app folder

urlpatterns = [
    path('admin/', admin.site.urls),
    path("projects/", include("projects.urls")), # this will add the urls inside projects app folder in here so django can use those urls
    path('',include('users.urls')) # any route that comes to users will be passed to user app urls
    ] # empty string is home page

urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL,document_root=settings.STATIC_ROOT) # linking url to static root
