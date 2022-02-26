#from django.db.models import query
from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages
#from django.contrib.auth import authenticate, login, logout
#from django.contrib.auth.models import User
from home.models import Contact
#from blog.models import Post

def home(request):
    return render(request, "home/home.html")
def about(request):
    return render(request, "home/about.html")
def contact(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        content = request.POST['content']
        print(name, email, phone, content)
        if len(name) < 2 or len(email) < 4 or len(phone) < 10 or len(content) < 3:
            messages.error(request, "Please fill the form correctly")

        else:
            contact = Contact(name=name, email=email, phone=phone, content=content)
            contact.save()
            messages.success(request, "Your message has been successfully sent")

    return render(request, "home/home.html")
