from asyncio import all_tasks
from distutils.command.build_scripts import first_line_re
from urllib import response
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, redirect
from django.http import HttpResponse 
from rest_framework.views import APIView
from .models import form
from django.contrib import admin



class API(APIView):
    def post(self,request):
        if request.method=="POST":
            # FirstName = request.POST.get('fname',None)
            # LastName = request.POST.get('lname',None)
            # Cnic = request.POST.get('Cnic',None)
            # DateOfBirth = request.POST.get('DOB',None)
            # Adress = request.POST.get('Adress',None)
            FirstName = request.data['fname']     # Use request.data to pass the data from json. json is a communication of backend to frontend
            LastName = request.data['lname']
            Cnic = request.data['Cnic']
            DateOfBirth = request.data['DOB']
            Adress = request.data['Adress']
            user = form(db_FirstName=FirstName,db_LastName=LastName,db_Cnic=Cnic,db_DOB=DateOfBirth,db_Adress=Adress)
            user.save()
     
        return render(request,'index.html')


class API2(APIView):
    def post(self,request):
        if request.method=="POST":
            FirstName = request.data['fname']    
            LastName = request.data['lname']
            Cnic = request.data['Cnic'] 
            DateOfBirth = request.data['DOB']
            Adress = request.data['Adress']
            formdata = form.objects.get(db_Cnic=Cnic)

            print(formdata)
            # user2 = form(formdata.db_FirstName=FirstName,formdata.db_LastName=LastName,formdata.db_Cnic=Cnic,db_DOB=DateOfBirth,db_Adress=Adress)
            # user2.save()

            formdata.db_FirstName = FirstName
            formdata.db_LastName = LastName
            formdata.db_Cnic = Cnic
            formdata.db_DOB = DateOfBirth
            formdata.db_Adress = Adress
            formdata.save()
    
        return render(request,'index.html')

    def get(self, request):
        return render(request,'index.html') 
        

# def delete(self,request):
#     Cnic = request.data['Cnic'] 
#     form.objects.get(db_Cnic=Cnic).delete()
#     allTasks = form.objects.all()     
#     data_info = {'data':allTasks}
#     return render(request,'display.html',data_info)   



def delete(contact_id):
    deleted = form.objects.get(db_Cnic=contact_id)
    deleted.delete()

    return redirect ('/')





def front(request):
    allTasks = form.objects.all()
    data_info = {'data':allTasks}
    return render(request,'display.html',data_info)    






         


# {
# "fname":"razaa",
# "lname":"Khan",
# "Cnic":"98765",
# "DOB":"24-08-1998",
# "Adress":"12123312"
# }
 

            











#class Form3(APIView):
#     def post(self,request):
#         if request.method=="POST":
#             # FirstName = request.POST.get('fname',None)
#             # LastName = request.POST.get('lname',None)
#             # Cnic = request.POST.get('Cnic',None)
#             # DateOfBirth = request.POST.get('DOB',None)
#             # Adress = request.POST.get('Adress',None)
#             FirstName = request.data['fname']     # Use request.data to pass the data from json. json is a communication of backend to frontend
#             LastName = request.data['lname']
#             Cnic = request.data['Cnic']
#             DateOfBirth = request.data['DOB']
#             Adress = request.data['Adress']
#             user = form(db_FirstName=FirstName,db_LastName=LastName,db_Cnic=Cnic,db_DOB=DateOfBirth,db_Adress=Adress)
#             user.save()
     
#         return render(request,'index.html')


                
    
   
# def home(request):
#     if request.method=="POST":
#         FirstName = request.POST.get('fname',None)
#         LastName = request.POST.get('lname',None)
#         Cnic = request.POST.get('Cnic',None)
#         DateOfBirth = request.POST.get('DOB',None)
#         Adress = request.POST.get('Adress',None)
#         user = form(db_FirstName=FirstName,db_LastName=LastName,db_Cnic=Cnic,db_DOB=DateOfBirth,db_Adress=Adress)
#         user.save()
     
#         return render(request,'index.html')
#     # return HttpResponse("Not found")


   
    

 
    

