from django.shortcuts import render
from Home.models import Contact,Blog

# Create your views here.
def index(request):
    # get all the blgos and sort it by created date on latest on top 
    blogs=Blog.objects.all().order_by('created_on')
    for blog in blogs:
        print(blog.author.username)
    context={'blogs':blogs}
    return render(request,'index.html',context)


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


def blog(request):

    posts=Blog.objects.all().order_by('created_on')
    context={'posts':posts}


    return render(request,'blog.html',context)


def blogpost(request,slug):
    blog=Blog.objects.filter(slug=slug).first()
    context={'blog':blog}
    return render(request,'blogpost.html',context)