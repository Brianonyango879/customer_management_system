from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .decorators import unauthenticated_user
from django.http import HttpResponse
from django.template.context_processors import request

from .forms import CustomUserCreationForm

# Create your views here.
@unauthenticated_user
def register_view(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,"Account Created Successfully")
            return redirect("login")
    else:
        form = CustomUserCreationForm()
    return render(request,'accounts/register.html',{'form':form})
@unauthenticated_user
def login_view(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        #check if user exist in the system with the above credentials
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect("home")
        else:
            messages.error(request,"Invalid Username or Password")
    return render(request, 'accounts/login.html')
#if a user is not logged in, our login.required decorator will redirect back to the login page
#else we allow the user to see the homepage
@login_required(login_url='login')
def home_view(request):
    return render(request, 'customer/dashboard.html')
def logout_view(request):
    logout(request)
    return redirect("login")
