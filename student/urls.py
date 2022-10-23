from django.urls import path
from . import views

app_name = "student"

urlpatterns = [
    path("", views.home, name="home"),
    path("student_home", views.student_home, name="student_home"),
    path("logout_user", views.logout_user, name="logout_user"), 
]