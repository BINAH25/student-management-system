from django.shortcuts import render,redirect
from django.contrib import messages
from student.models import *
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.core import serializers
import json

#from django.core.files.storage import FileSystemStorage

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
        #CHECK IF USERNAME ALREADY EXIST
        if CustomUser.objects.filter(username=username):
            messages.error(request, "Username Already Exist")
            return redirect(request.META.get("HTTP_REFERER"))
        
        #CHECK IF EMAIL ALREADY EXIST
        if CustomUser.objects.filter(email=email):
            messages.error(request, "Email Already Exist")
            return redirect(request.META.get("HTTP_REFERER"))

        try:
            user=CustomUser.objects.create_user(username=username,password=password,email=email,last_name=last_name,first_name=first_name,user_type=2)
            user.staffs.address=address
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
    session_years = SessionYear.objects.all()
    context = {
        'courses': courses,
        'session_years':session_years
    }
    if request.method == "POST":
        first_name=request.POST["first_name"]
        last_name=request.POST["last_name"]
        username=request.POST["username"]
        email=request.POST["email"]
        password=request.POST["password"]
        address=request.POST["address"]
        course_id=request.POST["course"]
        sex=request.POST["sex"]
        session_year = request.POST["session_year"]
        profile_pic = request.FILES["profile"]
        #CHECK IF USERNAME ALREADY EXIST
        if CustomUser.objects.filter(username=username):
            messages.error(request, "Username Already Exist")
            return redirect(request.META.get("HTTP_REFERER"))
        
        #CHECK IF EMAIL ALREADY EXIST
        if CustomUser.objects.filter(email=email):
            messages.error(request, "Email Already Exist")
            return redirect(request.META.get("HTTP_REFERER"))

        try:
            user=CustomUser.objects.create_user(username=username,password=password,email=email,last_name=last_name,first_name=first_name,user_type=3)
            user.students.address=address
            course_obj=Courses.objects.get(id=course_id)
            user.students.course_id=course_obj
            session_obj = SessionYear.objects.get(id=session_year)
            user.students.session_year=session_obj
            user.students.gender=sex
            user.students.profile_pic=profile_pic
            user.save()
            messages.success(request,"Successfully Added Student")
            return redirect(reverse("hod:add_student"))
        except:
            messages.error(request,"Failed to Add Student")
            return redirect(reverse("hod:add_student"))
    return render(request, 'hod/add_student.html',context)

def add_subject(request):
    courses = Courses.objects.all()
    staffs = CustomUser.objects.filter(user_type=2)
    context = {
        'courses': courses,
        'staffs':staffs
    }
    if request.method == "POST":
        subject_name=request.POST.get("subject_name")
        course_id=request.POST.get("course")
        course=Courses.objects.get(id=course_id)
        staff_id=request.POST.get("staff")
        staff=CustomUser.objects.get(id=staff_id)

        try:
            subject=Subjects(subject_name=subject_name,course_id=course,staff_id=staff)
            subject.save()
            messages.success(request,"Successfully Added Subject")
            return redirect(reverse("hod:add_subject"))
        except:
            messages.error(request,"Failed to Add Subject")
            return redirect(reverse("hod:add_subject"))

    return render(request, 'hod/add_subject.html',context)

def add_session(request):
    if request.method == "POST":
        session_start_year = request.POST["session_start_year"]
        session_end_year = request.POST["session_end_year"]
        try:
            session_year = SessionYear(session_start_year=session_start_year,session_end_year=session_end_year)
            session_year.save()
            messages.success(request,"Successfully Added add_session")
            return redirect(reverse("hod:add_session"))
        except:
            messages.error(request,"Failed to Add Session")
            return redirect(reverse("hod:add_session"))

       
    return render(request, 'hod/add_session.html')

def manage_staff(request):
    staffs=Staffs.objects.all()
    context = {
        'staffs':staffs
    }

    return render(request, 'hod/manage_staff.html', context)

def manage_student(request):
    students = CustomUser.objects.filter(user_type=3)
    context = {
        'students': students
    }
    return render(request, 'hod/manage_student.html',context)

def manage_subject(request):
    subjects = Subjects.objects.all()
    context = {
        'subjects': subjects
    }
    return render(request, 'hod/manage_subject.html',context)

def manage_course(request):
    courses = Courses.objects.all()
    context = {
        'courses': courses
    }
    return render(request, 'hod/manage_course.html', context)

def manage_session(request):
    session_years = SessionYear.objects.all()
    context = {
        'session_years': session_years
    }
    return render(request, 'hod/manage_session.html', context)

def edit_staff(request, pk):
    staff=Staffs.objects.get(id=pk)
    context = {
        'staff': staff
    }
    if request.method =="POST":
        admin_id=request.POST.get("admin_id")
        first_name=request.POST.get("first_name")
        last_name=request.POST.get("last_name")
        email=request.POST.get("email")
        username=request.POST.get("username")
        address=request.POST.get("address")
        try:
            user=CustomUser.objects.get(id=admin_id)
            user.first_name=first_name
            user.last_name=last_name
            user.email=email
            user.username=username
            user.save()

            staff_model=Staffs.objects.get(id=pk)
            staff_model.address=address
            staff_model.save()
            messages.success(request,"Successfully Edited Staff")
            return redirect(request.META.get("HTTP_REFERER"))
        except:
            messages.error(request,"Failed to Edit Staff")
            return redirect(request.META.get("HTTP_REFERER"))
        
    return render(request, 'hod/edit_staff.html', context)


def edit_student(request,pk):
    student = Students.objects.get(id=pk)
    courses = Courses.objects.all()
    session_years = SessionYear.objects.all()
    context = {
        'student': student,
        'courses':courses,
        'session_years':session_years
    }

    if request.method == "POST":
        first_name=request.POST["first_name"]
        last_name=request.POST["last_name"]
        username=request.POST["username"]
        email=request.POST["email"]
        address=request.POST["address"]
        course_id=request.POST["course"]
        sex=request.POST["sex"]
        session_year = request.POST["session_year"]
        admin_id = request.POST["admin_id"]
        profile_pic = request.FILES["profile"]
        try:
            user = CustomUser.objects.get(id=admin_id)
            user.first_name=first_name
            user.last_name=last_name
            user.email=email
            user.username=username
            user.save()

            session_obj = SessionYear.objects.get(id=session_year)
            student.session_year=session_obj
            student.address=address
            student.gender=sex
            course=Courses.objects.get(id=course_id)
            student.course_id=course
            student.profile_pic=profile_pic        
            student.save()
            messages.success(request,"Successfully Edited Student")
            return redirect(request.META.get("HTTP_REFERER"))
        except:
            messages.error(request,"Failed Edited Student")
            return redirect(request.META.get("HTTP_REFERER"))
       
      
    return render(request, 'hod/edit_student.html', context)


def edit_course(request,pk):
    course = Courses.objects.get(id=pk)
    context = {
        'course': course
    }
    if request.method == "POST":
        course_name = request.POST["course"]
        try:
            course.course_name=course_name
            course.save()
            messages.success(request,"Successfully Edited Course")
            return redirect(request.META.get("HTTP_REFERER"))
        except:
            messages.error(request,"Failed to Edit Course")
            return redirect(request.META.get("HTTP_REFERER"))

    return render(request, 'hod/edit_course.html',context)


def edit_subject(request,pk):
    subject = Subjects.objects.get(id=pk)
    courses = Courses.objects.all()
    staffs = CustomUser.objects.filter(user_type=2)
    context = {
        'subject': subject,
        'courses' : courses,
        'staffs': staffs
    }
    if request.method == "POST":
        subject_name = request.POST["subject_name"]
        course_id = request.POST["course"]
        staff_id = request.POST["staff"]
        staff = CustomUser.objects.get(id=staff_id)
        course = Courses.objects.get(id=course_id)
        try:
            subject.subject_name = subject_name
            subject.staff_id=staff
            subject.course_id=course
            subject.save()
            messages.success(request,"Successfully Edited Subject")
            return redirect(request.META.get("HTTP_REFERER"))
        except:
            messages.error(request,"Failed to Edit Subject")
            return redirect(request.META.get("HTTP_REFERER"))

    return render(request, 'hod/edit_subject.html',context)

def edit_session(request,pk):
    session_year = SessionYear.objects.get(id=pk)
    context = {
        'session_year':session_year
    }
    if request.method == "POST":
        session_start_year = request.POST["session_start_year"]
        session_end_year = request.POST["session_end_year"]
        try:
            session_year.session_start_year = session_start_year
            session_year.session_end_year = session_end_year
            session_year.save()
            messages.success(request,"Successfully Edited SessionYear")
            return redirect(request.META.get("HTTP_REFERER"))
        except:
            messages.error(request,"Failed to Edit SessionYear")
            return redirect(request.META.get("HTTP_REFERER"))

    return render(request, 'hod/edit_session.html',context)

def student_feedback_message(request):
    feedbacks=FeedBackStudent.objects.all()
    context = {
        'feedbacks':feedbacks
    }
    return render(request,'hod/student_feedback_message.html',context)

@csrf_exempt
def student_feedback_message_replied(request):
    feedback_id=request.POST.get("id")
    feedback_message=request.POST.get("message")

    try:
        feedback=FeedBackStudent.objects.get(id=feedback_id)
        feedback.feedback_reply=feedback_message
        feedback.save()
        return HttpResponse("True")
    except:
        return HttpResponse("False")

def staff_feedback_message(request):
    feedbacks=FeedBackStaffs.objects.all()
    context = {
        'feedbacks':feedbacks
    }
    return render(request,'hod/staff_feedback_message.html',context)

@csrf_exempt
def staff_feedback_message_replied(request):
    feedback_id=request.POST.get("id")
    feedback_message=request.POST.get("message")

    try:
        feedback=FeedBackStaffs.objects.get(id=feedback_id)
        feedback.feedback_reply=feedback_message
        feedback.save()
        return HttpResponse("True")
    except:
        return HttpResponse("False")

def student_leave_view(request):
    leaves = LeaveReportStudent.objects.all()
    context = {
        'leaves': leaves
    }
    return render(request,'hod/student_leave_view.html',context)

def student_approve_leave(request,pk):
    leave = LeaveReportStudent.objects.get(id=pk)
    leave.leave_status = 1
    leave.save()
    return redirect("hod:student_leave_view")

def student_disapprove_leave(request,pk):
    leave = LeaveReportStudent.objects.get(id=pk)
    leave.leave_status = 2
    leave.save()
    return redirect("hod:student_leave_view")

def staff_leave_view(request):
    leaves = LeaveReportStaff.objects.all()
    context = {
        'leaves': leaves
    }
    return render(request,'hod/staff_leave_view.html',context)

def staff_approve_leave(request,pk):
    leave = LeaveReportStaff.objects.get(id=pk)
    leave.leave_status = 1
    leave.save()
    return redirect("hod:student_leave_view")

def staff_disapprove_leave(request,pk):
    leave = LeaveReportStaff.objects.get(id=pk)
    leave.leave_status = 2
    leave.save()
    return redirect("hod:student_leave_view")

def admin_view_attendance(request):
    subjects=Subjects.objects.all()
    session_year_id=SessionYear.objects.all()
    context = {
        'subjects': subjects,
        'session_year_id':session_year_id
    }
    return render(request,"hod/admin_view_attendance.html",context)

@csrf_exempt
def admin_get_attendance_dates(request):
    subject=request.POST.get("subject")
    session_year_id=request.POST.get("session_year_id")
    subject_obj=Subjects.objects.get(id=subject)
    session_year_obj=SessionYear.objects.get(id=session_year_id)
    attendance=Attendance.objects.filter(subject_id=subject_obj,session_year=session_year_obj)
    attendance_obj=[]
    for attendance_single in attendance:
        data={"id":attendance_single.id,"attendance_date":str(attendance_single.attendance_date),"session_year_id":attendance_single.session_year.id}
        attendance_obj.append(data)

    return JsonResponse(json.dumps(attendance_obj),safe=False)


@csrf_exempt
def admin_get_attendance_student(request):
    attendance_date=request.POST.get("attendance_date")
    attendance=Attendance.objects.get(id=attendance_date)

    attendance_data=AttendanceReport.objects.filter(attendance_id=attendance)
    list_data=[]

    for student in attendance_data:
        data_small={"id":student.student_id.admin.id,"name":student.student_id.admin.first_name+" "+student.student_id.admin.last_name,"status":student.status}
        list_data.append(data_small)
    return JsonResponse(json.dumps(list_data),content_type="application/json",safe=False)

def admin_profile(request):
    user=CustomUser.objects.get(id=request.user.id)
    context ={
        'user': user
    }
    if request.method =="POST":
        first_name=request.POST.get("first_name")
        last_name=request.POST.get("last_name")
        username=request.POST.get("username")
        email=request.POST.get("email")
        password=request.POST.get("password")
        #try:
        user.first_name=first_name
        user.last_name=last_name
        user.username=username
        user.email=email
        # if password!=None and password!="":
        #     customuser.set_password(password)
        user.save()
        messages.success(request, "Successfully Updated Profile")
        return redirect("hod:admin_profile")
        
    return render(request,"hod/admin_profile.html",context)

