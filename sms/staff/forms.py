from django import forms
from staff.models import Staff, Staff_Login, Department, Classes, Subjects, Class_Timetable, Marks,Grade, Attendance
from student.models import Student
from django.contrib.auth.hashers import check_password

class StaffLoginForm(forms.Form):
    staff_id = forms.CharField(max_length=100, required=True)
    password = forms.CharField(widget=forms.PasswordInput, required=True)

    def clean(self):
        cleaned_data = super().clean()
        staff_id = cleaned_data.get("staff_id")
        password = cleaned_data.get("password")

        if not staff_id or not password:
            try:
                staff_login = Staff_Login.objects.get(staff_id=staff_id)
                if not check_password(password, staff_login.password):
                    raise forms.ValidationError("Invalid staff ID or password")
            except Staff_Login.DoesNotExist:
                raise forms.ValidationError("Invalid staff ID or password")
        return cleaned_data
    

class EditStudentProfileForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['name','father_name', 'mother_name', 'Dob', 'gender', 'email', 'phone','address', 'Education_10th', 'Education_12th', 'marks_10th', 'marks_12th', 'class_id', 'department_id', 'current_semester', 'photo']

class Attendance_entry(forms.Form):
    class_id = forms.CharField(widget=forms.HiddenInput())
    subject_id = forms.CharField(widget=forms.HiddenInput())
    department_id = forms.CharField(widget=forms.HiddenInput())
    date = forms.DateField(widget=forms.HiddenInput())
    period = forms.IntegerField(widget=forms.HiddenInput())

    def get_attendance_data(self):
        attendance = {}
        for key in self.data:
            if key.startswith('attendance_'):
                roll_no = key.split('_',1)[1]
                attendance[roll_no] = True
        return attendance
    
        
class ResultsEntryForm(forms.Form):
    class_id = forms.CharField(widget=forms.HiddenInput())
    subject_id = forms.CharField(widget=forms.HiddenInput())
    department_id = forms.CharField(widget=forms.HiddenInput())
    semester = forms.IntegerField(widget=forms.HiddenInput())

    def get_results_data(self):
        results = {}
        for key in self.data:
            if key.startswith('marks_'):
                roll_no = key.split('_',1)[1]
                marks_obtained = self.data.get(key)
                results[roll_no] = marks_obtained
        return results