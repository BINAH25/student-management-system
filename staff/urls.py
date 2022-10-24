from django.urls import path
from . import views

app_name = "staff"

urlpatterns = [
    path("", views.staff_home, name="staff_home"),
    path("attendance", views.attendance, name="attendance"),
    path("get_students", views.get_students, name="get_students"),
    path("save_attendance_data", views.save_attendance_data, name="save_attendance_data"),
    path("staff_update_attendance", views.staff_update_attendance, name="staff_update_attendance"),
    path("get_attendance_dates", views.get_attendance_dates, name="get_attendance_dates"),
    path("get_attendance_student", views.get_attendance_student, name="get_attendance_student"),
    path("save_updateattendance_data", views.save_updateattendance_data, name="save_updateattendance_data"),
    path("apply_for_leave", views.apply_for_leave, name="apply_for_leave"),
    path("staff_feedback", views.staff_feedback, name="staff_feedback"),
]