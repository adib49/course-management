from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username = username , password = password)

        if user is not None:
            login(request,user)

            if user.role == 'ADMIN':
                return redirect('admin_dashboard')
            
            elif user.role == 'INSTRUCTOR':
                return redirect('instructor_dashboard')
            
            else:
                return redirect('student_dashboard')
        else:
            messages.error(request,'Invalid Credentials')
        
        return render(request,'cms/login.html')

