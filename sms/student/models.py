from django.db import models

# Create your models here.
class Student(models.Model):
    roll_no = models.IntegerField(unique=True, primary_key=True)
    photo = models.ImageField(blank=True, null=True, upload_to='student_photos/',default='student_photos/default.jpeg')
    name = models.CharField(max_length=100)
    father_name = models.CharField(max_length=100)
    mother_name = models.CharField(max_length=100)
    Dob = models.DateField()
    gender = models.CharField(max_length=10,null=True, blank=True)
    email = models.EmailField(max_length=100)
    phone = models.BigIntegerField(blank=True, null=True)
    address = models.TextField()
    slug = models.SlugField(max_length=100, unique=True)
    Education_10th = models.CharField(max_length=100)
    Education_12th = models.CharField(max_length=100)
    marks_10th = models.FloatField(max_length=10, blank=True, null=True)
    marks_12th = models.FloatField(max_length=10, blank=True, null=True)
    class_id = models.ForeignKey('staff.Classes', on_delete=models.CASCADE, blank=True, null=True)
    department_id = models.ForeignKey('staff.Department', on_delete=models.CASCADE, blank=True, null=True)
    class_teacher_id = models.ForeignKey('staff.Staff', on_delete=models.CASCADE, blank=True, null=True)
    current_semester = models.IntegerField(blank=True,null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.name} ({self.roll_no})"
    

class Student_Login(models.Model):
    student_id = models.AutoField(unique=True, primary_key=True)
    roll_no = models.ForeignKey('student.Student', on_delete=models.CASCADE, blank=True, null=True)
    password = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"login for {self.roll_no} ({self.password}): {self.student_id})"
    
