from django.shortcuts import render,redirect
from django.contrib import messages
from student.models import *
from django.urls import reverse

# Create your views here.

def hod_home(request):
    return render(request,'hod/home.html')

def add_staff(request):
    if request.method =="POST":
        first_name=request.POST.get("first_name")
        last_name=request.POST.get("last_name")
        username=request.POST.get("username")
        email=request.POST.get("email")
        password=request.POST.get("password")
        address=request.POST.get("address")

        try:
            user=CustomUser.objects.create_user(username=username,password=password,email=email,last_name=last_name,first_name=first_name,user_type=2)
            user.save()
            messages.success(request,"Successfully Added Staff")
            return redirect(reverse('hod:add_staff'))
        except:
            messages.error(request,"Failed to Add Staff")
            return redirect(reverse('hod:add_staff'))

    return render(request,'hod/add_staff.html')

def add_course(request):
    if request.method =="POST":
        get_course=request.POST.get("course")
        try:
            course = Courses(course_name=get_course)
            course.save()
            messages.success(request,"Course added")
            return redirect(reverse('hod:add_course'))
        except:
            messages.error(request,"Failed to Add course")
            return redirect(reverse('hod:add_course'))

    
    return render(request, 'hod/add_course.html')

def add_student(request):
    courses = Courses.objects.all()
    context = {
        'courses': courses
    }
    if request.method == "POST":
        first_name=request.POST["first_name"]
        last_name=request.POST["last_name"]
        username=request.POST["username"]
        email=request.POST["email"]
        password=request.POST["password"]
        address=request.POST["address"]
        session_start=request.POST["session_start"]
        session_end=request.POST["session_end"]
        course_id=request.POST["course"]
        sex=request.POST["sex"]

        #try:
        user=CustomUser.objects.create_user(username=username,password=password,email=email,last_name=last_name,first_name=first_name,user_type=3)
        #user.students.address=address
        #course_obj=Courses.objects.get(id=course_id)
        #user.students.course_id=course_obj
        #user.students.session_start_year=session_start
        #user.students.session_end_year=session_end
        #user.students.gender=sex
        #user.students.profile_pic=""
        user.save()
        messages.success(request,"Successfully Added Student")
        return redirect(reverse("hod:add_student"))
        #except:
            #messages.error(request,"Failed to Add Student")
            #return redirect(reverse("hod:add_student"))
    return render(request, 'hod/add_student.html',context)

