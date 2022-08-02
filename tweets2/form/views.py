from audioop import add
from cProfile import label
from email.generator import DecodedGenerator
from queue import Empty
from tkinter.ttk import LabeledScale
from types import TracebackType
from urllib import response
from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
import pandas as pd 
import json 
import csv
import pymongo
from pymongo import MongoClient
import ast
from requests import head
from rest_framework.views import APIView
from django.core.paginator import Paginator, EmptyPage
from .models import Posts, Labels

# Create your views here.
#mongodb+srv://@<CLUSTER>/<COLLECTION>?ssl=true&ssl_cert_reqs=CERT_NONE
client = pymongo.MongoClient("mongodb://localhost27017" , connect=False)

def cleanedData(db_field, dataList):
    if len(dataList) == 0:
        return [{db_field: None}]

    else:
        link = []
        for i in range(len(dataList)):
            link.append({db_field: dataList[i]})
                
        return link

def uploadCsv(request):
    csvfile = open('final.csv', 'r', encoding="UTF-8")
    reader = csv.DictReader(csvfile)
    mongo_client=MongoClient() 

    db=mongo_client.tweet1
    db.form_posts.drop()
    header= ["date", "time", "timezone", "user_id", "username", "name", "language", "mentions", "urls", "photos", "hashtags", "replies_count", "retweets_count", "likes_count", "content_Link", "content"]

    for each in reader:
        #convert strings into list
        each["mentions"] = ast.literal_eval(each["mentions"])

        if len(each["mentions"]) == 0 :
            each["mentions"] = [{'screen_name': 'null', 'name': 'null', 'id':"null"}]

        each["urls"] = ast.literal_eval(each["urls"])
        each["urls"] = cleanedData("urls", each["urls"])

        each["hashtags"] = ast.literal_eval(each["hashtags"])
        each["hashtags"] = cleanedData("hashtags", each["hashtags"])

        each["photos"] = ast.literal_eval(each["photos"])
        each["photos"] = cleanedData("photos", each["photos"])
       
        row={}
        for field in header:
            row[field]=each[field]
        db.form_posts.insert(row)

    return HttpResponse("uploaded")

def index(request):
    l = Posts.objects.all()
    for p in l:
        print(p.content_link)
    #p = Paginator(post_items, 20)
    # page = p.page(2)

    # context = {'items': page}

    return render(request,'paginator.html')







def show(request):
    posts=Posts.objects.all()    
 

    for p in posts:
        a = p.mentions
        b = ast.literal_eval(a)
        
        if len(b)>0:
            print(b[0]['screen_name'])

    return HttpResponse('hello show')


class Login(APIView):
    def post(self,request):
        posts = Posts.objects.all()
        for p in posts:
            print(p.username)
        labler = Labels.objects.all()


        # for p in posts:
        #     print(p.name)

        #allTasks = posts

        # for p in labler:
        #     print(labler)

        tweetdata = {'tweetdata':posts, 'Labels':labler}
        #labelers = {}


        #json 

        return render(request,'sample2.html',tweetdata)
    
# get input from user in a new htmlfile 
# for our label table and save the input in
# label table.


class pont(APIView):
    def post(self,request):
       # if request.method == "POST":
        UpLabel = request.POST.get('fname',None)
            #print(Labels)
        user = Labels(label=UpLabel)
        user.save()

        return render(request,'sample2.html')

            # user = Labels.objects.all()
            # user.save()

    #def get(self, request):
class AddLabel(APIView):    
    def post(self, request):
        label = request.POST.get('label',None)
        user = Labels(label=label)
        user.save()

class Labelling(APIView):
    def post(self,request):
        if request.method=="POST":
            # mydata=POST.obects.all()
            link = request.POST.get('link',None) #"abc/abc"
            label = request.POST.get('label',None) #offensive
            print(label)
            user1 = Labels.objects.get(label=label)
            print(link, label)
            user2 = Posts.objects.get(content_Link=link)
            print(user1.id)
            print(user2)


            user2.label.add(user1.id)
        

            # didi = request.POST.get('lname',None)
            # muser = POST(content_link=didi) 
            # muser.save() 




 
            return render(request,'sample.html')

    def get(self, request):
        return render(request,'sample.html')
    




# never use filter 

            

# def Labelling(request):
#     libil = Labels.objects.get(user_id)
#     print(libil)

#     return render(request,"sample.html")


def AddManual(request):

    l = Labels(label=[{'label':'weapon'}])
    l.save()
   
    # myobj = Labels()
    # myobj.labels=['weapon']
    # myobj.save()

    # labels_instance = Labels.objects.create(label="weapon")
    # labels_instance.save()
  
    return render(request,'sample.html')

def lists(request):
    p = Posts.objects.all()
    for i in p :
        print(i.content_link)
    


    return render(request,'sample.html')


def paginate(request):
    pt = Posts.objects.all()

    p = Paginator(pt, 5)

    page_num = request.GET.get('page', 1)

    try:
        page = p.page(page_num)
    except EmptyPage:
        page = p.page(1)    


    context = {'items': page}


    return render(request,'paginator.html',context)
    
    

import json 

python_data={'name':'adnan','roll':'8'}
json_data = json.dumps(python_data)

print(json_data)


            

  







# load = pd.read_csv('form/final.csv')
# load.head()
# print(load)

# def SaveData(request):
   

#     return HttpResponse('hello')

