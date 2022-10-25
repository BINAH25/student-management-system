from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .EmailBackEnd import *
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib import messages
from student.models import *
import datetime

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

def student_view_attendance(request):
    student=Students.objects.get(admin=request.user.id)
    course=student.course_id
    subjects=Subjects.objects.filter(course_id=course)
    context = {
        'subjects':subjects
    }
    return render(request,"student/view_attendance.html",context)

def student_view_attendance_post(request):
    subject_id=request.POST.get("subject")
    start_date=request.POST.get("start_date")
    end_date=request.POST.get("end_date")

    start_data_parse=datetime.datetime.strptime(start_date,"%Y-%m-%d").date()
    end_data_parse=datetime.datetime.strptime(end_date,"%Y-%m-%d").date()
    subject_obj=Subjects.objects.get(id=subject_id)
    user_object=CustomUser.objects.get(id=request.user.id)
    stud_obj=Students.objects.get(admin=user_object)

    attendance=Attendance.objects.filter(attendance_date__range=(start_data_parse,end_data_parse),subject_id=subject_obj)
    attendance_reports=AttendanceReport.objects.filter(attendance_id__in=attendance,student_id=stud_obj)
    context = {
        'attendance_reports':attendance_reports
    }
    return render(request,"student/attendance_data.html",context)
