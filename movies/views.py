from typing_extensions import Required
from django.http.response import HttpResponse
from django.shortcuts import render
from django.http import HttpRequest
from .models import movies

def index(request):
    allmove=movies.objects.all()
    param={"allmove":allmove}

    return render(request,'index.html',param)
def login(request):
    return render(request,'login/index.html')
def movieView(request,myid):
    movie = movies.objects.filter(movie_id=myid)

    return render(request,"mView.html",{'movie':movie[0]})