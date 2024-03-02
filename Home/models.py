from django.db import models
from froala_editor.fields import FroalaField
from Home.utils import slug_generator

# Create your models here.
class Blog(models.Model):
    title = models.CharField(max_length=1000)
    content= FroalaField()
    slug=models.SlugField(max_length=1000,unique=True,blank=True,null=True)
    image=models.ImageField(upload_to='blog/')
    created_on=models.DateTimeField(auto_now_add=True)
    updated_on=models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
    
    def save(self,*args,**kwargs):
        self.slug=slug_generator(self.title)
        print("********* received slug in models.")
        print(self.slug)
        super(Blog,self).save(*args,**kwargs)