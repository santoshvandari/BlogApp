from django.urls import path
from Home import views




urlpatterns = [
    path('',views.index,name='index'),
    path('home/',views.index,name='index'),
    path('about/',views.about,name='about'),
    path('contact/',views.contact,name='contact'),
    path('team/',views.team,name='team'),
    path('blog/',views.blog,name='blog'),
    path('blog/<slug>',views.blogpost,name='blogpost')
]