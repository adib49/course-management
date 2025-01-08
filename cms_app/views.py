from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Course

def add_course(request):
    if request.user.role != 'INSTRUCTOR':
        messages.error(request,"Access Denied")
        return redirect('cms_app:login')
    
    if request.method == 'POST':
        title = request.POST.get('title')
        course_code = request.POST.get('course_code')
        content = request.POST.get('content')

        Course.objects.create(
            title = title,
            course_code = course_code,
            content = content,
            instructor = request.user
        )
        messages.success(request,'Course added successfully')
        return redirect ('cms_app:instructor_dashboard')
    
    return redirect ('cms_app:instructor_dashboard')





@login_required
def student_dashboard(request):
    if request.user.role != 'STUDENT':
        messages.error('Access Denied')
        return redirect('cms_app:login')
    
    enrolled_courses = request.user.enrolled_courses.all()

    context = {
        'courses': enrolled_courses,
        'student': request.user
    }
    return render(request,'cms_app/student_dashboard.html',context)

@login_required
def instrcutor_dashboard(request):
    if request.user.role != 'INSTRUCTOR':
        messages.error('Access Denied')
        return redirect('cms_app:login')
    
    teaching_courses = request.user.teaching_courses.all()

    context = {
        'courses':teaching_courses,
        'instructor':request.user
    }
    return render(request,'cms_app/instructor_dashboard.html',context)

def login_view(request):
        
    if request.method == 'POST':
        print("POST data:", request.POST)
        username = request.POST.get('username')
        password = request.POST.get('password')
        print(f"Atempting to login with username: {username} and password: {password}")

        user = authenticate(username = username , password = password)

        if user is not None:
            login(request,user)

            if user.role == 'ADMIN':
                return redirect('cms_app:admin_dashboard')
            
            elif user.role == 'INSTRUCTOR':
                return redirect('cms_app:instructor_dashboard')
            
            else:
                return redirect('cms_app:student_dashboard')
        else:
            messages.error(request,'Invalid Credentials')
        
    return render(request,'cms_app/login.html')

def logout_view(request):
    logout(request)
    return redirect('cms_app:login')
