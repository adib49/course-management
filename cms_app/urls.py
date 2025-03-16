from django.urls import path
from . import views

app_name = 'cms_app'
urlpatterns = [
    path('', views.login_view, name='login'),
    path('student-dashboard/', views.student_dashboard, name='student_dashboard'),
    path('instructor-dashboard/', views.instrcutor_dashboard, name='instructor_dashboard'),
    path('admin-dashboard/', views.admin_dashboard, name='admin_dashboard'),
    path('add_course/',views.add_course,name='add_course'),
    path('logout/', views.logout_view, name='logout'),
    path('edit-course/<int:course_id>/', views.edit_course, name='edit_course'),
    path('delete-course/<int:course_id>/', views.delete_course, name='delete_course'),
    path('assign-students/<int:course_id>/', views.assign_students, name='assign_students'),
]