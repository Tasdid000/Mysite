from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages
from home.models import *
from django.shortcuts import get_object_or_404


def home(request):
    allposts = certificate.objects.all()
    context = {'allposts': allposts}
    return render(request, "home/home.html", context)


def about(request):
    allposts = certificate.objects.all()
    context = {'allposts': allposts}
    return render(request, "home/about.html", context)


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
            contact = Contact(name=name, email=email,
                              phone=phone, content=content)
            contact.save()
            messages.success(
                request, "Your message has been successfully sent")

    return render(request, "home/contact.html")


def download_cv(request, sno):
    cv_entry = get_object_or_404(cv, sno=sno)
    file_path = cv_entry.cv.path
    with open(file_path, 'rb') as f:
        # Adjust the content type as per your file type
        response = HttpResponse(f.read(), content_type='application/pdf')
        # Adjust the filename as needed
        response['Content-Disposition'] = 'attachment; filename="cv.pdf"'
        return response
