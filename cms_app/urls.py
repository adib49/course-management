from django.urls import path
from . import views

app_name = 'cms_app'
urlpatterns = [
    path('', views.login_view, name='login'),
    path('student-dashboard/', views.student_dashboard, name='student_dashboard'),
    path('instructor-dashboard/', views.instrcutor_dashboard, name='instructor_dashboard'),
    path('add_course/',views.add_course,name='add_course'),
    path('logout/', views.logout_view, name='logout'),
]