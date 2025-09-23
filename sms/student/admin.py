from django.contrib import admin
from .models import Student

# Register your models here.
class StudentDetail(admin.ModelAdmin):
    list_display = ('name','email','department_id','class_id','class_teacher_id')
    search_fields = ['roll_no','department_id__department_id','class_id__class_id']
    list_filter = ['department_id__department_id','class_id__class_id']

admin.site.register(Student,StudentDetail)