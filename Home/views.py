from django.shortcuts import render,redirect
from Home.models import Contact,Blog
from django.core.paginator import Paginator
from django.contrib.auth import logout

# Create your views here.
def index(request):
    blogs=Blog.objects.all().order_by('created_on')
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
    blog_list = Blog.objects.all()
    paginator = Paginator(blog_list, 6)  # Show 6 blogs per page
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
        'posts': page_obj,
    }
    return render(request,'blog.html',context)

def blogpost(request,slug):
    blog=Blog.objects.filter(slug=slug).first()
    if blog is None:
        return render(request,'404.html')
    posts=Blog.objects.all().order_by('created_on')[:4]
    context={'blog':blog,'posts':posts}
    return render(request,'blogpost.html',context)

def custom_404(request, exception):
    return render(request, '404.html', status=404)