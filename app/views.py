from django.shortcuts import render,redirect

# Create your views here.
def index(request):
    #return redirect("index")
    return render(request,"app/index.html")