from django.contrib import admin
from Home.models import Blog

# Register your models here.

# display list 
class BlogAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_on')
    search_fields = ['title', 'content']

admin.site.register(Blog, BlogAdmin)
