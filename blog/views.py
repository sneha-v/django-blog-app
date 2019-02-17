from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from blog.models import Post

def home(request):
    all_mod= Post.objects.all()
    return render(request,"home.html", {"all_mod":all_mod})

def blah(request):
    return HttpResponse("WE SHALL OVERCOME BLAH BLAH")
def about(request):
    return render(request, "about.html",{'myname':'name'})

def create(request):
    if request.method=="POST":
        return render(request, "about.html",{"myname":request.POST["field"]})
    return render(request,"create.html")
