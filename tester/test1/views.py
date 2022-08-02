from logging import exception
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from test1.serializer import StudentsSerializer
from .models import Student
from rest_framework.renderers import JSONRenderer
from rest_framework import serializers
from rest_framework.views import APIView
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.generics import GenericAPIView
from rest_framework.mixins import ListModelMixin, CreateModelMixin, RetrieveModelMixin, DestroyModelMixin, UpdateModelMixin
from rest_framework import viewsets




# Create your views here.
def index(request):
    return render(request,'index.html')


class API1(APIView):
    def post(self,request):
        try:
            n1 = int(float(request.POST.get('lname')))
            n2 = int(float(request.POST.get('lroll')))  
            if n1>10:
                user=(n1+n2)    
            else:
                user=(n1-n2)          
            print(user)
            params = {'ans':user}
        except ValueError:
            params = {'ans':'Only int bitch'}

            print('Only Integer Value . not string')    
        return render(request,'index.html',params)


    def get(self, request):
        return render(request,'index.html',) 
        


class Login(APIView):
    def post(self,request):
        stu = Student.objects.all()
        serializer = StudentsSerializer(stu)
        json_data = JSONRenderer().render(serializer.data)	 		 # then we convertd python native data into json 
        autehntication_class = [BasicAuthentication]
        permission_class = [IsAuthenticated]
        return HttpResponse(json_data, content_type = 'application/json')	 # first we put json_data to our response and then tell the content that we are sending json data 'application/json'
            

# List and Create - PK not required 

class LCStudentList(GenericAPIView, ListModelMixin, CreateModelMixin):
    queryset = Student.objects.all()
    serializer_class = StudentsSerializer

    def get(self, request, *args, **kwargs):
        print(args,kwargs)
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs) 

# Retrieve Update and Delete - PK Required

class RUDStudentList(GenericAPIView, RetrieveModelMixin, UpdateModelMixin, DestroyModelMixin):
    queryset = Student.objects.all()
    serializer_class = StudentsSerializer

    def get(self, request, *args, **kwargs):
        print(args,kwargs)
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)    

    


class StudentModelViewSet(viewsets.ModelViewSet, CreateModelMixin):
    queryset = Student.objects.all()
    serializer_class = StudentsSerializer







        
       
