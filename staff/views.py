from django.shortcuts import render, redirect
from student.models import *
from django.views.decorators.csrf import csrf_exempt
from django.core import serializers
import json
from django.contrib import messages
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse

# Create your views here.
def staff_home(request):
    return render(request,'staff/home.html')



def attendance(request):
    subjects=Subjects.objects.filter(staff_id=request.user.id)
    session_years = SessionYear.objects.all()
    context = {
        "subjects": subjects,
        "session_years": session_years
    }    
    return render(request,'staff/attendance.html',context)

@csrf_exempt
def get_students(request):
    subject_id=request.POST.get("subject")
    session_year=request.POST.get("session_year")

    subject=Subjects.objects.get(id=subject_id)
    session_model=SessionYear.objects.get(id=session_year)
    students=Students.objects.filter(course_id=subject.course_id,session_year_id=session_model)
    list_data=[]

    for student in students:
        data_small={"id":student.admin.id,"name":student.admin.first_name+" "+student.admin.last_name}
        list_data.append(data_small)
    return JsonResponse(json.dumps(list_data),content_type="application/json",safe=False)

@csrf_exempt
def save_attendance_data(request):
    student_ids=request.POST.get("student_ids")
    subject_id=request.POST.get("subject_id")
    attendance_date=request.POST.get("attendance_date")
    session_year_id=request.POST.get("session_year_id")

    subject_model=Subjects.objects.get(id=subject_id)
    session_model=SessionYear.objects.get(id=session_year_id)
    json_sstudent=json.loads(student_ids)
    #print(data[0]['id'])

    try:
        attendance=Attendance(subject_id=subject_model,attendance_date=attendance_date,session_year=session_model)
        attendance.save()

        for stud in json_sstudent:
                student=Students.objects.get(admin=stud['id'])
                attendance_report=AttendanceReport(student_id=student,attendance_id=attendance,status=stud['status'])
                attendance_report.save()
        return HttpResponse("OK")
    except:
        return HttpResponse("ERR")

def staff_update_attendance(request):
    subjects=Subjects.objects.filter(staff_id=request.user.id)
    session_year_id=SessionYear.objects.all()
    context = {
        "subjects":subjects,
        "session_year_id":session_year_id
    }
    return render(request,"staff/update_attendance.html", context)

@csrf_exempt
def get_attendance_dates(request):
    subject=request.POST.get("subject")
    session_year_id=request.POST.get("session_year_id")
    subject_obj=Subjects.objects.get(id=subject)
    session_year_obj=SessionYear.object.get(id=session_year_id)
    attendance=Attendance.objects.filter(subject_id=subject_obj,session_year_id=session_year_obj)
    attendance_obj=[]
    for attendance_single in attendance:
        data={"id":attendance_single.id,"attendance_date":str(attendance_single.attendance_date),"session_year_id":attendance_single.session_year_id.id}
        attendance_obj.append(data)

    return JsonResponse(json.dumps(attendance_obj),safe=False)

@csrf_exempt
def get_attendance_student(request):
    attendance_date=request.POST.get("attendance_date")
    attendance=Attendance.objects.get(id=attendance_date)

    attendance_data=AttendanceReport.objects.filter(attendance_id=attendance)
    list_data=[]

    for student in attendance_data:
        data_small={"id":student.student_id.admin.id,"name":student.student_id.admin.first_name+" "+student.student_id.admin.last_name,"status":student.status}
        list_data.append(data_small)
    return JsonResponse(json.dumps(list_data),content_type="application/json",safe=False)

@csrf_exempt
def save_updateattendance_data(request):
    student_ids=request.POST.get("student_ids")
    attendance_date=request.POST.get("attendance_date")
    attendance=Attendance.objects.get(id=attendance_date)

    json_sstudent=json.loads(student_ids)


    try:
        for stud in json_sstudent:
             student=Students.objects.get(admin=stud['id'])
             attendance_report=AttendanceReport.objects.get(student_id=student,attendance_id=attendance)
             attendance_report.status=stud['status']
             attendance_report.save()
        return HttpResponse("OK")
    except:
        return HttpResponse("ERR")

def apply_for_leave(request):
    staff = Staffs.objects.get(admin=request.user.id)
    leave_data = LeaveReportStaff.objects.filter(staff_id=staff)
    context = {
        'leave_data': leave_data
    }
    if request.method == "POST":
        leave_date = request.POST['leave_date']
        leave_msg = request.POST['leave_msg']
        try:
            report = LeaveReportStaff(staff_id=staff,leave_date=leave_date,leave_message=leave_msg,leave_status=0)
            report.save()
            messages.success(request,"Successfully Requested for Leave ")
            return redirect("staff:apply_for_leave")
        except:
            messages.error(request,"Failed to Request for leave ")
            return redirect("staff:apply_for_leave")
        
    return render(request, 'staff/apply_for_leave.html', context)

def staff_feedback(request):
    staff = Staffs.objects.get(admin=request.user.id)
    feedback_data = FeedBackStaffs.objects.filter(staff_id=staff)
    context = {
        'feedback_data':feedback_data
    }
    if request.method == "POST":
        feedback_msg = request.POST['feedback_msg']
        try:
            feedback = FeedBackStaffs(staff_id=staff,feedback=feedback_msg,feedback_reply="")
            feedback.save()
            messages.success(request,"Successfully ask for feedback ")
            return redirect("staff:staff_feedback")
        except:
            messages.error(request,"Failed to add feedback ")
            return redirect("staff:staff_feedback")
        
    return render(request,'staff/feedback.html', context)