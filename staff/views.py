from django.shortcuts import render, redirect
from student.models import *

# Create your views here.
def staff_home(request):
    return render(request,'staff_home.html')