from django.urls import path
from . import views

app_name = "hod"

urlpatterns = [
    path("", views.hod_home, name="hod_home"),
    path("add_staff", views.add_staff, name="add_staff"),
    path("add_course", views.add_course, name="add_course"),
    path("add_student", views.add_student, name="add_student"),
    
]