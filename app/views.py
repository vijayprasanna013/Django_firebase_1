from django.shortcuts import render,redirect
#import pyrebase
import os

# Create your views here.
""" config = {
    "apiKey": "AIzaSyCYZugIp7w9s75W61K6kk1HOFhaKGV1Qc4",

    "authDomain": "django-test-1-d4b92.firebaseapp.com",

    "projectId": "django-test-1-d4b92",

    "storageBucket": "django-test-1-d4b92.appspot.com",

    "messagingSenderId": "644116425430",

    "appId": "1:644116425430:web:2379973b285e0eb9eaf777",

    "measurementId": "G-5Z924L84EY"


}

firebase = pyrebase.initialize_app(config)
storage = firebase.storage()
database=firebase.database() """


def index(request):
    #return redirect("index")
    return render(request,"app/index.html")