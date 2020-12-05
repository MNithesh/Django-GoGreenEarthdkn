from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from .models import Contact
# Email import
from django.core.mail import send_mail
from django.conf import settings
from django.core import mail
from django.core.mail.message import EmailMessage
# Create your views here.
def index(request):
    return render(request,'index.html')


def signup(request):
    if request.method=="POST":
        user_name=request.POST['username']
        first_name=request.POST['fname']
        last_name=request.POST['lname']
        email=request.POST['email']
        password=request.POST['pass1']
        confirm_password=request.POST['pass2']
        if password!=confirm_password:
            messages.warning(request,"Password not matching")
            return render(request,'signup.html')
        try:
            if User.objects.get(username=user_name):
                messages.warning(request,"Username already taken")
                return render(request,'signup.html')
        except Exception as identifier:
            pass
        try:
            if User.objects.get(email=email):
                messages.warning(request,"Email already taken")
                return render(request,'signup.html')
        except Exception as identifier:
            pass
        myuser=User.objects.create_user(user_name,email,password)
        myuser.first_name=first_name
        myuser.last_name=last_name
        myuser.save()
        messages.info(request,"SignUp Success!")
    return render(request,'signup.html')


def contact(request):
    if request.method=="POST":
        fname=request.POST.get('name')
        femail=request.POST.get('email')
        fnumb=request.POST.get('num')
        fdesc=request.POST.get('desc')
        #print(name,email,numb,desc)
        query=Contact(name=fname,email=femail,ph_no=fnumb,desc=fdesc)
        query.save()
        messages.info(request,"Submit Success!")
    return render(request,'contact.html')

def about(request):
    return render(request,'about.html')


def search(request):
    query=request.GET['search']
    if len(query)>78:
        allPosts=Blogs.objects.none()
    else:
        allPostsTitle=Blogs.objects.filter(title__icontains=query)
        allPostsContent=Blogs.objects.filter(description__icontains=query)
        allPosts=allPostsTitle.union(allPostsContent)

    if allPosts.count()== 0:
        messages.warning(request,"No Search Results")

    params={'allPosts':allPosts,'query':query}   
     
    return render(request,'search.html',params)