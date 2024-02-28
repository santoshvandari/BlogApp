from django.db import models
from froala_editor.fields import FroalaField

# Create your models here.
class Blog(models.Model):
    title = models.CharField(max_length=1000)
    content= FroalaField()


    def __str__(self):
        return self.title