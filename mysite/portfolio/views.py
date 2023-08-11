from .models import *
from django.contrib import messages
from django.shortcuts import render, HttpResponse, redirect



# Create your views here.

def portfolioHome(request):
    allposts = portfolio.objects.all()
    context = {'allposts': allposts}
    return render(request, "portfolio/portfolioHome.html", context)

def portfolioPost(request, slug):
    post = portfolio.objects.filter(slug=slug).first()
    print=(request.user)
    context = {'post': post, "user": request.user}
    return render(request, "portfolio/portfolioPost.html", context)
