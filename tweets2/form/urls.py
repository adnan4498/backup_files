"""tweets2 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from django.urls import path
from .import views
from .views import Login,pont,Labelling,AddLabel

urlpatterns = [
    path('index/',views.index,name='index'),
    path('show/',views.show,name='show'),
    path("Login/",Login.as_view()),
    path("pont/",pont.as_view()),
    path("Labelling/",Labelling.as_view()),
    path('AddLabel',AddLabel.as_view()),
    path('upload/',views.uploadCsv,name='upload'),
    path('manual/',views.AddManual,name='manual'),
    path('lists/',views.lists,name='lists'),
    path('paginate/',views.paginate,name='paginate')
   
]