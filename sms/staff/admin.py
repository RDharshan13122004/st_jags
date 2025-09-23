from django.contrib import admin
from staff.models import *

# Register your models here. 
class PostStaff(admin.ModelAdmin):
    list_display = ('staff_id','staff_name','staff_email','staff_phone','department_id','staff_designation')
    search_fields = ['staff_id','class_id__class_name','staff_name','department_id__department_name','department_id__department_id']
    list_filter = ['department_id__department_id','class_id__class_name']

admin.site.register(Staff, PostStaff)
admin.site.register(OurPage)
admin.site.register(ImageTable)