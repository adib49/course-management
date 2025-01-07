from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required

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
