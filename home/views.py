#from django.db.models import query
from django.shortcuts import render, HttpResponse, redirect
#from django.contrib import messages
#from django.contrib.auth import authenticate, login, logout
#from django.contrib.auth.models import User
#from home.models import Contact
#from blog.models import Post

def home(request):
    return render(request, "home/home.html")
def about(request):
    return render(request, "home/about.html")
def contact(request):
    return render(request, "home/contact.html")
def join(request):
    return render(request, "home/join.html")

