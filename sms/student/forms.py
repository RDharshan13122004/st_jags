from django import forms
from student.models import Student_Login,Student
from django.contrib.auth.hashers import check_password


class StudentLoginForm(forms.Form):
    student_id = forms.IntegerField(required=True)
    password = forms.CharField(widget=forms.PasswordInput, required=True)

    def clean(self):
        cleaned_data = super().clean()
        student_id = cleaned_data.get("student_id")
        password = cleaned_data.get("password")
        if student_id and password:
            try:
                student_login = Student_Login.objects.get(roll_no = student_id)
                if not check_password(password, student_login.password):    
                    raise forms.ValidationError("Invalid roll number or password")
            except Student_Login.DoesNotExist:
                raise forms.ValidationError("Invalid roll number or password")
        return cleaned_data

class AttendanceForm(forms.Form):
    from_date = forms.DateField(required=False, widget=forms.DateInput(attrs={'type': 'date'}))
    to_date = forms.DateField(required=False, widget=forms.DateInput(attrs={'type': 'date'}))
    VIEW_CHOICES = [
        ('table', 'Table'),
        ('time', 'Time Graph'),
        ('pie', 'Pie Graph'),
        ('plot', 'Plot'),
    ]
    view = forms.ChoiceField(choices=VIEW_CHOICES, widget=forms.RadioSelect, required=True)
    def clean(self):
        cleaned_data = super().clean()
        from_date = cleaned_data.get("from_date")
        to_date = cleaned_data.get("to_date")
        
        if from_date and to_date and from_date > to_date:
            raise forms.ValidationError("From date cannot be later than To date")
        return cleaned_data