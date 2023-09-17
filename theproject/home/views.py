from django.shortcuts import render
from services.models import ourServices

# Create your views here.

    

def homePage(request):
    services = ourServices.objects.all()
    context = {
        "services":services
    }
    return render(request, 'home/index.html',context)

def aboutPage(request):
    return render(request, 'home/about.html')

def blogPage(request):
    return render(request, 'home/blog.html')

def contactPage(request):
    return render(request, 'home/contact.html')

