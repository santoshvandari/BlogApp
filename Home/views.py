from django.shortcuts import render
from Home.models import Contact

# Create your views here.
def index(request):
    return render(request,'index.html')


def about(request):
    return render(request,'about.html')


def contact(request):
    if request.method=='POST':
        name=(request.POST['name']).strip()
        email=(request.POST['email']).strip()
        subject=(request.POST['subject']).strip()
        message=(request.POST['message']).strip()
        contact=Contact(name=name,email=email,subject=subject,message=message)
        contact.save()
    return render(request,'contact.html')


def team(request):
    return render(request,'team.html')

def blog(request):
    return render(request,'blog.html')