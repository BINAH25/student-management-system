from django.urls import path
from . import views

app_name = "hod"

urlpatterns = [
    path("", views.hod_home, name="hod_home"),
    path("add_staff", views.add_staff, name="add_staff"),
    path("add_course", views.add_course, name="add_course"),
    path("add_student", views.add_student, name="add_student"),
    path("add_subject", views.add_subject, name="add_subject"),
    path("manage_staff", views.manage_staff, name="manage_staff"),
    path("manage_student", views.manage_student, name="manage_student"),
    path("manage_subject", views.manage_subject, name="manage_subject"),
    path("manage_course", views.manage_course, name="manage_course"),
    path("edit_staff/<int:pk>", views.edit_staff,name="edit_staff"),
    path("edit_student/<int:pk>", views.edit_student,name="edit_student"),
    path("edit_course/<int:pk>", views.edit_course, name="edit_course"),
    path("edit_subject/<int:pk>", views.edit_subject, name="edit_subject"),

    
]