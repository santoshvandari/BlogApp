from django.contrib import admin
from Home.models import Blog,Contact

# Register your models here.

# display list 
class BlogAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_on')
    search_fields = ['title', 'content']


class ContactAdmin(admin.ModelAdmin):
    list_display = ('id','name', 'email', 'subject', 'created_on')

admin.site.register(Blog, BlogAdmin)
admin.site.register(Contact, ContactAdmin)
