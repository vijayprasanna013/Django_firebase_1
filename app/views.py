""" from django.shortcuts import render, redirect
from django.shortcuts import render
from django.conf import settings
from django.core.files.storage import default_storage
from django.contrib import messages
import pyrebase
import os
from .models import * """
from django.shortcuts import render
import pyrebase
import os
from .models import *
# Create your views here.
config = {
    "apiKey": "AIzaSyCn3Z1sKiPxGnsz1TEx045nqSVLrcnNBeE",
    "authDomain": "djnago-test-a8d6a.firebaseapp.com",
    "databaseURL": "https://djnago-test-a8d6a-default-rtdb.firebaseio.com",
    "projectId": "djnago-test-a8d6a",
    "storageBucket": "djnago-test-a8d6a.appspot.com",
    "messagingSenderId": "476181580554",
    "appId": "1:476181580554:web:715f06722b5e2369ccc8f3"

}
# app_name/views.py

firebase = pyrebase.initialize_app(config)
# Get a reference to the database
db = firebase.database()

storage = firebase.storage()

""" def main(request):
    if request.method == 'POST':
        file = request.FILES['file']
        file_save = default_storage.save(file.name, file)
        storage.child("files/" + file.name).put("media/" + file.name)
        delete = default_storage.delete(file.name)
        messages.success(request, "File upload in Firebase Storage successful")
        return redirect('main')
    else:
        return render(request, 'main.html')

 """

def index(request):
    if request.method == 'POST':
        print("ECHO")
    else:
        return render(request, 'app/index.html')