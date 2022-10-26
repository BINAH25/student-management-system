from django.urls import path
from . import views

app_name = "student"

urlpatterns = [
    path("", views.home, name="home"),
    path("student_home", views.student_home, name="student_home"),
    path("logout_user", views.logout_user, name="logout_user"), 
    path("student_view_attendance", views.student_view_attendance, name="student_view_attendance"), 
    path("student_view_attendance_post", views.student_view_attendance_post, name="student_view_attendance_post"),
    path("student_apply_for_leave", views.student_apply_for_leave, name="student_apply_for_leave"),
    path("student_feedback", views.student_feedback, name="student_feedback"), 
]