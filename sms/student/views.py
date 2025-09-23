from django.shortcuts import render,redirect,get_object_or_404
from django.http import HttpResponse
from django.urls import reverse
from student.models import Student, Student_Login
from staff.models import Class_Timetable, Subjects,Staff,OurPage,ImageTable, Attendance, Marks, Department, Grade
from django.contrib.auth import logout
from student.forms import StudentLoginForm, AttendanceForm
from django.contrib.auth.hashers import check_password
from django.contrib.auth.decorators import login_required
from datetime import datetime

# Create your views here.

# def test(request):
#     return HttpResponse("This is a test view in the student app.")

def index(request):
    ourpage = OurPage.objects.get(page="index")
    images = ImageTable.objects.filter(page_id=ourpage)
    return render(request,'student/index.html',
                  {
                    'page_image':images,
                    })

def bba_depart(request):
    ourpage = OurPage.objects.get(page="BBA")
    images = ImageTable.objects.filter(page_id=ourpage)
    staff_details = Staff.objects.filter(department_id='BBA')
    return render(request, 'student/bba_depart.html',
                  {
                    'staff_detail':staff_details,
                    'facilities_img': images,
                  })

def aero_space(request):
    ourpage = OurPage.objects.get(page="aero")
    images = ImageTable.objects.filter(page_id=ourpage)
    return render(request, 'student/aero_space_depart.html',{
        'facilities_img': images,
    })

def bca(request):
    ourpage = OurPage.objects.get(page="bca")
    images = ImageTable.objects.filter(page_id=ourpage)
    return render(request, 'student/bca_depart.html',{
        'facilities_img': images,
    })

def cse(request):
    staff_details = Staff.objects.filter(department_id='BECSE')

    ourpage = OurPage.objects.get(page="becse")
    images = ImageTable.objects.filter(page_id=ourpage)
    return render(request, 'student/cs_depart.html',{
        'staff_detail': staff_details,
        'facilities_img': images,
    })

def eee(request):
    ourpage = OurPage.objects.get(page="eee")
    images = ImageTable.objects.filter(page_id=ourpage)
    return render(request, 'student/eee_depart.html',{
        'facilities_img': images,
    })

def eng(request):
    ourpage = OurPage.objects.get(page="eng")
    images = ImageTable.objects.filter(page_id=ourpage)
    staff_details = Staff.objects.filter(department_id='ENGLIS')
    return render(request, 'student/eng_depart.html',{
        'staff_detail':staff_details,
        'facilities_img': images,
    })

def math(request):
    ourpage = OurPage.objects.get(page="bscmat")
    images = ImageTable.objects.filter(page_id=ourpage)
    staff_details = Staff.objects.filter(department_id='BSCMAT')
    return render(request, 'student/math_depart.html',
                  {
                    'staff_detail':staff_details,
                    'facilities_img': images,
                  })

def mechanical(request):
    staff_details = Staff.objects.filter(department_id='MECH')

    ourpage = OurPage.objects.get(page="mech")
    images = ImageTable.objects.filter(page_id=ourpage)
    return render(request, 'student/mech_depart.html'
                  ,{
                    'staff_detail':staff_details,
                    'facilities_img': images,
                  })


def get_grade_point(grade_name: str) -> int:
    """Map grade name to grade points (adjust if your grading scheme differs)."""
    grade_points = {
        "O": 10,
        "A": 9,
        "B": 8,
        "C": 7,
        "D": 6,
        "E": 5,
        "F": 0,
    }
    return grade_points.get(grade_name, 0)


def sgpa(student, semester):
    """Calculate SGPA for a student in a given semester."""
    semester_results = Marks.objects.filter(roll_no=student.roll_no, semester=semester)

    total_points = 0
    total_credits = 0

    for result in semester_results.select_related("subject_id", "grade_obtained"):
        if not result.grade_obtained:  # skip if no grade assigned
            continue
        grade_point = get_grade_point(result.grade_obtained.grade_name)
        credits = result.subject_id.credits
        total_points += grade_point * credits
        total_credits += credits

    if total_credits == 0:
        return 0
    return round(total_points / total_credits, 2)


def cgpa(student):
    """Calculate CGPA for a student across all semesters."""
    all_results = Marks.objects.filter(roll_no=student.roll_no)

    total_points = 0
    total_credits = 0

    for result in all_results.select_related("subject_id", "grade_obtained"):
        if not result.grade_obtained:
            continue
        grade_point = get_grade_point(result.grade_obtained.grade_name)
        credits = result.subject_id.credits
        total_points += grade_point * credits
        total_credits += credits

    if total_credits == 0:
        return 0
    return round(total_points / total_credits, 2)



def student_dashboard(request, slug):
    #checks is the sessions exists
    if 'student_slug' not in request.session:
        return redirect(reverse("student:student_login"))
    
    #timetable
    student = get_object_or_404(Student, slug=slug)
    timetable_entries = Class_Timetable.objects.filter(class_id=student.class_id).order_by('day','period')
    days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']
    timetable = {day: ['']*6 for day in days}
    subject_count = Subjects.objects.filter(department_id=student.department_id,semester = student.current_semester).count()
    for entry in timetable_entries:
        subject = entry.subject_id.subject_name if entry.subject_id else "---"
        staff = entry.staff_id.staff_name if entry.staff_id else ""
        display = f"{subject}<br><span class='staff-name'>{staff}</span>"
        if entry.day in timetable and entry.period in range(1, 7):
            timetable[entry.day][entry.period - 1] = display

    #get sections        
    show_section = request.GET.get('section','')

    #attendance info
    form = AttendanceForm()   # always available
    attendance_records = Attendance.objects.filter(roll_no_id=student.roll_no).order_by('date', 'period')

    # default states
    show_table = show_time = show_pie = show_plot = False
    view_option = None

    if request.method == "POST":
        form = AttendanceForm(request.POST)
        print(f"DEBUG: Received POST request with data: {request.POST}")
        if form.is_valid():
            from_date = form.cleaned_data.get('from_date')
            to_date = form.cleaned_data.get('to_date')
            view_option = form.cleaned_data.get('view')
            print(f"DEBUG: Form is valid. from_date={from_date}, to_date={to_date}, view_option={view_option}")

            if from_date:
                attendance_records = attendance_records.filter(date__gte=from_date)
            if to_date:
                attendance_records = attendance_records.filter(date__lte=to_date)

            show_table = view_option == "table"
            show_time = view_option == "time"
            show_pie = view_option == "pie"
            show_plot = view_option == "plot"
        else:
            print(f"DEBUG: Form errors = {form.errors}")
    else:
        show_table = True
        view_option = "table"

    print(f"DEBUG: Total attendance records = {attendance_records.count()}")
    print(f"DEBUG: show_table={show_table}, show_time={show_time}, show_pie={show_pie}, show_plot={show_plot}")

     # Calculate chart data
    present_count = attendance_records.filter(status="Present").count()
    absent_count = attendance_records.filter(status="Absent").count()
    
    print(f"DEBUG: present_count={present_count}, absent_count={absent_count}")
    
    # Get ordered records for chart data
    ordered_records = attendance_records.order_by('date')
    dates_list = [str(record.date) for record in ordered_records]
    statuses_list = [1 if record.status == "Present" else 0 for record in ordered_records]
    
    print(f"DEBUG: dates_list = {dates_list}")
    print(f"DEBUG: statuses_list = {statuses_list}")
    print(f"DEBUG: request.path = {request.path}")
    chart_data = {
        "present": present_count,
        "absent": absent_count,
        "dates": dates_list,
        "statuses": statuses_list,
    }
    
    #Result Section
    get_semester = request.GET.get('semester','')

    show_section = request.GET.get('section','')
    if get_semester and not show_section:
        show_section = 'results'
    
    results_context = {}
    print(f"DEBUG: student.department_id = {student.department_id}")
    depart_semester = Department.objects.filter(department_id=student.department_id.department_id).first()
    print(f"DEBUG: depart_semester = {depart_semester}")

    semesters_range = []
    if depart_semester:
        semesters_range = range(1, depart_semester.no_of_semesters + 1)
    if get_semester:

        print(f"DEBUG: Semester selected = {get_semester}")

        semester_results = Marks.objects.filter(roll_no_id = student.roll_no, semester = get_semester)

        cgpa_value = cgpa(student)
        sgpa_value = sgpa(student, get_semester)
        print(depart_semester.no_of_semesters)
        results_context = {
            "results": semester_results,
            "cgpa": cgpa_value,
            "sgpa": sgpa_value,
        }


    return render(request, 'student/student_dashboard.html', {
        'student': student,
        'timetable': timetable,
        'subject_count': subject_count,
        'show_section': show_section,
        'form': form,
        "attendance_records": attendance_records,
        "show_table": show_table,
        "show_pie": show_pie,
        "show_time": show_time,
        "show_plot": show_plot,
        "chart_data": chart_data,
        "semesters": semesters_range,
        **results_context,
    })

def student_login(request):
    form = StudentLoginForm()
    if request.method == 'POST':
        form = StudentLoginForm(request.POST)
        if form.is_valid():
            roll_no = form.cleaned_data['student_id']
            password = form.cleaned_data['password']
            try:
                students_login = Student_Login.objects.get(roll_no=roll_no)
                if check_password(password, students_login.password):
                    student = Student.objects.get(roll_no=roll_no)
                    request.session['student_slug'] = student.slug
                    return redirect(reverse('student:student_dashboard', args=[student.slug]))
            except Student_Login.DoesNotExist:
                return render(request, 'student/login_signin.html', {'form': form, 'error': 'Invalid roll number or password'})
        return render(request, 'student/login_signin.html', {'form': form})

    return render(request, 'student/login_signin.html')

def student_register(request):
    return render(request, 'student/student_registion.html')

def student_profile(request,slug):
    student = Student.objects.filter(slug=slug).first()
    if not student:
        return HttpResponse("Student not found", status=404)
    return render(request, 'student/profile_page.html', {
        'student': student
    })

def student_logout(request):
    logout(request)
    return redirect(reverse('student:student_login'))  