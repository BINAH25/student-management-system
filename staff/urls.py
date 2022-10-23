from django.urls import path
from . import views

app_name = "staff"

urlpatterns = [
    path("", views.staff_home, name="staff_home"),
    path("attendance", views.attendance, name="attendance"),
    path("get_students", views.get_students, name="get_students"),
    path("save_attendance_data", views.save_attendance_data, name="save_attendance_data"),

]