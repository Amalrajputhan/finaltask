from django.contrib import messages, auth
from django.contrib.auth.models import User
from django import forms
from django.http import HttpResponse
from django.shortcuts import render, redirect
# from .forms import STOREModelform
from django import forms
from django.shortcuts import render


def amal(request):
    return render(request,"amal.html")
def register (request):
    if request.method=="POST":
        username=request.POST['username']
        # first_name = request.POST['first_name']
        # last_name=request.POST['last_name']
        # email=request.POST['email']
        password=request.POST['password']
        cpassword=request.POST['password1']
        if password==cpassword:
            if User.objects.filter(username=username).exists():
                messages.info(request,"user name Taken")
                return redirect('register')
            # elif User.objects.filter(email=email).exists():
            #     messages.info(request, "email already taken")
            #     return redirect('register')
            else:

                user=User.objects.create_user(username=username,password=password)
                # first_name = first_name, last_name = last_name, email = email
                user.save();
                return redirect('login')

        else:
            messages.info(request, "password not matching")
            return redirect('register')
        return redirect('login')
    return  render(request,"register.html")
def login(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        user=auth.authenticate(username=username,password=password)

        if user is not None:
            auth.login(request,user)
            # return redirect('/')
            return redirect('/')
            # return render(request, "last.html")
        else:
            messages.info(request,"invalid credentials")
            return  redirect('login')
    return  render(request,"login.html")

def logout(request):
    auth.logout(request)
    return redirect('/')
# def prof(request):
#   return render(request,"welcome.html")

def Home(request):
    return redirect('/')