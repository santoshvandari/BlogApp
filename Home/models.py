from django.db import models
from froala_editor.fields import FroalaField
from Home.utils import slug_generator
from django.contrib.auth.models import User

# Create your models here.
class Blog(models.Model):
    title = models.CharField(max_length=1000)
    content= FroalaField()
    slug=models.SlugField(max_length=1000,unique=True,blank=True,null=True)
    # author=models.ForeignKey(User,blank=False,on_delete=models.CASCADE)
    author = models.ForeignKey(User,blank=False,null=True,on_delete=models.CASCADE)
    image=models.ImageField(upload_to='blog/')
    created_on=models.DateTimeField(auto_now_add=True)
    updated_on=models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
    
    def save(self,*args,**kwargs):
        self.slug=slug_generator(self.title)
        super(Blog,self).save(*args,**kwargs)

class Contact(models.Model):
    name=models.CharField(max_length=100)
    email=models.EmailField(max_length=100)
    subject=models.CharField(max_length=500)
    message=models.TextField()
    created_on=models.DateTimeField(auto_now_add=True)