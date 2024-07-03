from django.shortcuts import render,redirect
from .models import Account
from django.contrib import messages,auth
from .forms import *

from django.contrib.auth.decorators import login_required

from django.contrib.auth import authenticate,login,logout
# Create your views here.
from django.urls import reverse


def register(request):
    if request.method=="POST":
            user=Account.objects.filter(email=request.POST['email'])
            if user.exists():
                  messages.info(request,'User aready exist')
                  return redirect(reverse('accounts:register'))
            form=RegistrationForm(request.POST)
            if form.is_valid():
                  first_name = form.cleaned_data['first_name']
                  last_name = form.cleaned_data['last_name']
                  email = form.cleaned_data['email']
                  password = form.cleaned_data['password']
                  username=form.cleaned_data['username']
                  user=Account.objects.create_user(first_name=first_name,last_name=last_name,username=username,email=email,password=password)
                  user.save()
                  return redirect(reverse('accounts:login'))
    f=RegistrationForm()
    return render(request,'register.html',context={'form':f})


def login_view(request):
    if request.method=='POST':
            email=request.POST['email']
            password=request.POST['password']
            form=LoginForm(request.POST)
            if form.is_valid():
                user=auth.authenticate(email=email,password=password)
                print(user)
                if user is not None:
                      auth.login(request,user)
                      return redirect(reverse('store:store'))
                else:
                      messages.error(request,'Invalid username or password')
                      return redirect(reverse('accounts:login'))
    f=LoginForm()
    return render(request,'login.html',context={'form':f})