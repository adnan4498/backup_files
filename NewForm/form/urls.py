from ast import Delete
from django.contrib import admin
from django.urls import path, include
from .import views
from .views import API2, API


urlpatterns = [
    path("api/",API.as_view()),
    path("api2/",API2.as_view()),
    path("front/",views.front,name='display'),
    path("delete/<contact_id>",views.delete,name="delete")
    #path("home/", views.home, name="home"), 
]



#  {

#  "fname":"adnan",
#  "lname":"kkhan",
#  "Cnic":"12321",
#  "DOB":"asdasd",
#  "Adress":"aasdasaasdaa"


#  }