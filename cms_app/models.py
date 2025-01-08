from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    ROLES = (
        ('ADMIN','Admin'),
        ('INSTRUCTOR','Instructor'),
        ('STUDENT','Student')
    )
    
    role = models.CharField(max_length = 20, choices = ROLES)
    unique_code = models.CharField(max_length = 5, unique = True, null= True , blank = True)

class Course(models.Model):
    title = models.CharField(max_length = 30)
    content = models.CharField(max_length = 200)
    course_code = models.CharField(max_length = 5, unique=True )
    created_at = models.DateTimeField(auto_now_add= True)
    instructor = models.ForeignKey(CustomUser, on_delete = models.CASCADE, related_name='teaching_courses')
    student = models.ManyToManyField(CustomUser, related_name = 'enrolled_courses')

    