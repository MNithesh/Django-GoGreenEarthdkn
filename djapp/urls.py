from django.contrib import admin
from django.urls import path,include
from djapp import views

urlpatterns = [
    path('',views.index,name='index'),
    path('search',views.search,name='search'),
    path('contact',views.contact,name='contact'),
    path('signup',views.signup,name='signup'),
    path('about',views.about,name='about'),
]
