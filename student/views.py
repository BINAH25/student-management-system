from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .EmailBackEnd import *
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib import messages

# Create your views here.
def student_home(request):
    return render(request, 'student/home.html')

def home(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        user = EmailBackEnd.authenticate(request,username=email,password=password)
        if user !=None:
            print(user)
            login(request,user)
            if user.user_type=="1":
                return redirect('hod:hod_home')
            elif user.user_type=="2":
                return redirect('staff:staff_home')
            elif user.user_type=="3":
                return redirect('student:student_home')
            else:
                messages.error(request,"Invalid Login Details")
        else:
            messages.error(request,"Invalid Login Details")
            return redirect("student:home")

    return render(request, 'login.html')

def logout_user(request):
    logout(request)
    return redirect("student:home")