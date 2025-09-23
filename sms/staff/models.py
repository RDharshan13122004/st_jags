from django.db import models

# Create your models here.
class Staff(models.Model):
    staff_id = models.CharField(max_length=10, unique=True, primary_key=True)
    staff_name = models.CharField(max_length=100)
    staff_email = models.EmailField(max_length=100)
    staff_phone = models.BigIntegerField(blank=True, null=True)
    staff_address = models.TextField()
    staff_DOB = models.DateField()
    gender = models.CharField(max_length=10)
    staff_photo = models.ImageField(blank=True, null=True, upload_to='staff_photos/',default='staff_photos/default.jpeg')
    staff_designation = models.CharField(max_length=50)
    class_id = models.ForeignKey('staff.Classes', on_delete=models.CASCADE, null=True, blank=True)
    department_id = models.ForeignKey('staff.Department', on_delete=models.CASCADE, blank= True, null=True)
    slug = models.SlugField(max_length=100, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.staff_name} ({self.staff_id})"
    
class Staff_Login(models.Model):
    staff_log_id = models.AutoField(primary_key=True)
    staff_id = models.ForeignKey('staff.Staff', on_delete=models.CASCADE, blank= True, null=True)
    password = models.CharField(max_length=100)

    def __str__(self):
        return f"Login for {self.staff_id} ({self.staff_log_id})"
    

class Department(models.Model):
    department_id = models.CharField(max_length=10, unique=True, primary_key=True)
    department_name = models.CharField(max_length=100)
    no_of_semesters = models.IntegerField(default=1)

    def __str__(self):
        return f"{self.department_name} ({self.department_id})"
    
class Classes(models.Model):
    class_id = models.CharField(max_length=10, unique=True, primary_key=True)
    class_name = models.CharField(max_length=100)
    department_id = models.ForeignKey('staff.Department', on_delete=models.CASCADE, blank= True, null=True)
    class_teacher_id = models.ForeignKey('staff.Staff', on_delete=models.CASCADE, blank= True, null=True)
    no_of_students = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.class_name} ({self.class_id})"

class Subjects(models.Model): 
    subject_id = models.CharField(max_length=10, unique=True, primary_key=True)
    subject_name = models.CharField(max_length=100)
    credits = models.FloatField(max_length=10,blank=True,null=True)
    department_id = models.ForeignKey('staff.Department', on_delete=models.CASCADE, blank= True, null=True)
    semester = models.IntegerField(default=1)

    def __str__(self):
        return f"{self.subject_id} {self.subject_name}"
    

class Class_Timetable(models.Model):
    table_id  = models.AutoField(unique=True, primary_key=True)
    class_id = models.ForeignKey('staff.Classes', on_delete=models.CASCADE, blank= True, null=True)
    staff_id = models.ForeignKey('staff.Staff', on_delete=models.CASCADE, blank= True, null=True)
    subject_id = models.ForeignKey('staff.Subjects', on_delete=models.CASCADE, blank= True, null=True)
    department_id = models.ForeignKey('staff.Department', on_delete=models.CASCADE, blank= True, null=True)
    day = models.CharField(max_length=10, choices=[
        ('Monday', 'Monday'),
        ('Tuesday', 'Tuesday'),
        ('Wednesday', 'Wednesday'),
        ('Thursday', 'Thursday'),
        ('Friday', 'Friday'),])
    period = models.IntegerField(blank=True, null=True)  # e.g., 1, 2, 3, etc.
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Timetable for {self.class_id} on {self.day} ({self.table_id})"

class Marks(models.Model):
    mark_id = models.AutoField(primary_key=True,unique=True)
    subject_id = models.ForeignKey(Subjects, on_delete=models.CASCADE, blank= True, null=True)
    roll_no = models.ForeignKey('student.Student', on_delete=models.CASCADE, blank= True, null=True)
    marks_obtained = models.FloatField()
    grade_obtained = models.ForeignKey('staff.Grade', on_delete=models.CASCADE, blank= True, null=True)
    total_marks = models.FloatField(default=100)
    class_id = models.ForeignKey('staff.Classes', on_delete=models.CASCADE, blank= True, null=True)
    department_id = models.ForeignKey('staff.Department', on_delete=models.CASCADE, blank= True, null=True)
    semester = models.IntegerField(default=1)

    def __str__(self):
        return f"Marks for {self.roll_no} in {self.subject_id} ({self.mark_id})"

class Attendance(models.Model):
    attendance_id = models.AutoField(unique=True, primary_key=True)
    roll_no = models.ForeignKey('student.Student', on_delete=models.CASCADE, blank= True, null=True)
    class_id = models.ForeignKey('staff.Classes', on_delete=models.CASCADE, blank= True, null=True)
    department_id = models.ForeignKey('staff.Department', on_delete=models.CASCADE, blank= True, null=True)
    subject_id = models.ForeignKey('staff.Subjects', on_delete=models.CASCADE, blank= True, null=True)
    staff_id = models.ForeignKey('staff.Staff', on_delete=models.CASCADE, blank= True, null=True)
    date = models.DateField()
    period = models.IntegerField(blank=True,null=True)
    status = models.CharField(max_length=10, default="incomplete")  # e.g., 'Present', 'Absent'
    attendance_start_date = models.DateField(default='2025-08-01')
    attendance_ended_date = models.DateField(default='2025-10-12')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Attendance for {self.roll_no} on {self.date} ({self.attendance_id})"
    
class OurPage(models.Model):
    page = models.CharField(primary_key=True,max_length=200)
    
class ImageTable(models.Model):
    page = models.ForeignKey('staff.OurPage',on_delete=models.CASCADE,blank=True,null=True)
    section = models.CharField(max_length=200,blank=True,null=True)
    image = models.ImageField(max_length=200,blank=True, null=True,upload_to="page_image/")

class Grade(models.Model):
    grade_id = models.AutoField(primary_key=True)
    grade_name = models.CharField(max_length=1)  # e.g., 'A', 'B', etc.
    min_percentage = models.FloatField()  # Minimum percentage for this grade
    max_percentage = models.FloatField()  # Maximum percentage for this grade

    def __str__(self):
        return f"{self.grade_name} ({self.min_percentage}-{self.max_percentage}%)"