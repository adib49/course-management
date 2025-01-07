from django.urls import path
from . import views

app_name = 'cms_app'
urlpatterns = [
    path('', views.login_view, name='login'),
    path('student-dashboard/', views.student_dashboard, name='student_dashboard'),
    path('logout/', views.logout_view, name='logout'),
]