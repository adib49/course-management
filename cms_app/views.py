from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Course,CustomUser
from .forms import CustomUserForm

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
def admin_dashboard(request):
    if request.user.role != 'ADMIN':
        messages.error('Access Denied')
        return redirect('cms_app:login')
    
    all_courses = Course.objects.all()
    all_user = CustomUser.objects.all()

    if request.method == 'POST':
        if 'add_user' in request.POST:
            user_form = CustomUserForm(request.POST)
            if user_form.is_valid():
                user_form.save()
                messages.success(request, 'User added successfully.')
                return redirect('cms_app:admin_dashboard')

        elif 'update_user' in request.POST:
            user_id = request.POST.get('user_id')
            user = get_object_or_404(CustomUser, id=user_id)
            user_form = CustomUserForm(request.POST, instance=user)
            if user_form.is_valid():
                user_form.save()
                messages.success(request, 'User updated successfully.')
                return redirect('cms_app:admin_dashboard')

        elif 'delete_user' in request.POST:
            user_id = request.POST.get('user_id')
            user = get_object_or_404(CustomUser, id=user_id)
            user.delete()
            messages.success(request, 'User deleted successfully.')
            return redirect('cms_app:admin_dashboard')

    else:
        user_form = CustomUserForm()

    context = {
        'courses': all_courses,
        'users': all_user,
        'admin': request.user,
        'user_form': user_form
    }
    return render(request,'cms_app/admin_dashboard.html',context)

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
