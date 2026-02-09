"""
URL configuration for meeting_planner project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
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
from django.urls import path, include

from website.views import about, welcome
import django.contrib.auth.urls 
#^^control + click the urls part to see the relevant helper functions and the behind the scenes magic
#you should see that it's expecting a auth/login/ route, but we have not created a view or template for this

urlpatterns = [
    path('admin/', admin.site.urls),
    path('about/', about, name="about"),
    path('meetings/',include('meetings.urls')), 
    path('', welcome, name="welcome"),
    path('auth/', include('django.contrib.auth.urls')),
]
