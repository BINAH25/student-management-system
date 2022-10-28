from django.urls import path
from . import views

app_name = "hod"

urlpatterns = [
    path("", views.hod_home, name="hod_home"),
    path("add_staff", views.add_staff, name="add_staff"),
    path("add_course", views.add_course, name="add_course"),
    path("add_student", views.add_student, name="add_student"),
    path("add_session", views.add_session, name="add_session"),
    path("add_subject", views.add_subject, name="add_subject"),
    path("manage_staff", views.manage_staff, name="manage_staff"),
    path("manage_student", views.manage_student, name="manage_student"),
    path("manage_subject", views.manage_subject, name="manage_subject"),
    path("manage_course", views.manage_course, name="manage_course"),
    path("manage_session", views.manage_session, name="manage_session"),
    path("edit_staff/<int:pk>", views.edit_staff,name="edit_staff"),
    path("edit_student/<int:pk>", views.edit_student,name="edit_student"),
    path("edit_course/<int:pk>", views.edit_course, name="edit_course"),
    path("edit_subject/<int:pk>", views.edit_subject, name="edit_subject"),
    path("edit_session/<int:pk>", views.edit_session, name="edit_session"),
    path("student_leave_view", views.student_leave_view, name="student_leave_view"),
    path("student_approve_leave/<int:pk>", views.student_approve_leave, name="student_approve_leave"),
    path("student_disapprove_leave/<int:pk>", views.student_disapprove_leave, name="student_disapprove_leave"),
    path("student_feedback_message", views.student_feedback_message, name="student_feedback_message"),
    path("staff_leave_view", views.staff_leave_view, name="staff_leave_view"),
    path("staff_approve_leave/<int:pk>", views.staff_approve_leave, name="staff_approve_leave"),
    path("staff_disapprove_leave/<int:pk>", views.staff_disapprove_leave, name="staff_disapprove_leave"),
    path("student_feedback_message", views.student_feedback_message, name="student_feedback_message"),
    path("staff_feedback_message", views.staff_feedback_message, name="staff_feedback_message"),
    path("student_feedback_message_replied", views.student_feedback_message_replied, name="student_feedback_message_replied"),
    path("staff_feedback_message_replied", views.staff_feedback_message_replied, name="staff_feedback_message_replied"), 
    path("admin_view_attendance", views.admin_view_attendance, name="admin_view_attendance"), 
    path("admin_get_attendance_student", views.admin_get_attendance_student, name="admin_get_attendance_student"), 
    path("admin_get_attendance_dates", views.admin_get_attendance_dates, name="admin_get_attendance_dates"), 
    path("admin_profile", views.admin_profile, name="admin_profile"), 
]