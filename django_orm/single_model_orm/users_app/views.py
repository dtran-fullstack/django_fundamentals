from django.shortcuts import render, redirect
from .models import User
from django.db import models

# Create your views here.

def index(request):
    context = {
        'users' : User.objects.all()
    }
    return render(request,'index.html',context)

def create(request):
    User.objects.create(
        first_name=request.POST['first_name'],
        last_name=request.POST['last_name'],
        email_address=request.POST['email'],
        age=request.POST['age']
    )
    return redirect('/')

def delete(request):
    User.objects.get(id=request.POST['delete_user']).delete()
    return redirect('/')