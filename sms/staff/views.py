from django.shortcuts import render,redirect,get_object_or_404
from django.http import HttpResponse
from staff.models import Staff , Staff_Login, Class_Timetable, Classes,Department, Subjects, Attendance, Grade, Marks
from student.models import Student
from django.urls import reverse
from django.contrib.auth import logout
from django.contrib.auth.hashers import check_password
from django.utils.text import slugify
from staff.forms import StaffLoginForm, EditStudentProfileForm, Attendance_entry, ResultsEntryForm
from datetime import datetime, date ,timedelta
from uuid import uuid4
import calendar
# Create your views here.

def test(request):
    return HttpResponse("This is a test view in the staff app.")


def staff_dashboard(request,slug):
    if 'staff_slug' not in request.session:
        return redirect(reverse('staff:staff_login'))

    #staff details
    staff = get_object_or_404(Staff, slug=slug)

    #timetable details
    timetable_entries = Class_Timetable.objects.filter(staff_id=staff.staff_id).order_by('day','period')
    days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']
    timetable = {day: ['']*6 for day in days}
    for entry in timetable_entries:
        subject = entry.subject_id.subject_name if entry.subject_id else "---"
        class_name = entry.class_id.class_name if entry.class_id else""
        display = f"{subject}<br><span class=''>{class_name}</span>"
        if entry.day in timetable and entry.period in range(1, 7):
            timetable[entry.day][entry.period - 1] = display

    #student records
    students_record = Student.objects.filter(class_id=staff.class_id).order_by('roll_no')

    # Get the section to show from the request
    show_section = request.GET.get('section', '')

    # === Attendance Logic ===
    start_date = Attendance._meta.get_field('attendance_start_date').default
    start_date = date.fromisoformat(start_date)
    end_date = date.today()

    class_cards = []
    current_date = start_date
    while current_date <= end_date:
        weekday = current_date.strftime('%A') 
        if weekday not in ['Saturday','Sunday']:
            attendance_entry_detail = Class_Timetable.objects.filter(staff_id=staff,
                                                                     day = weekday
                                                                     ).select_related(
                                                                         'class_id',
                                                                         'subject_id',
                                                                         'department_id')
            for entry in attendance_entry_detail:
                class_student = Student.objects.filter(class_id = entry.class_id)
                status_check = Attendance.objects.filter(class_id=entry.class_id,
                                                         subject_id=entry.subject_id,
                                                         date = current_date,
                                                         period = entry.period
                                                         )
                if status_check:
                    status= "completed"
                else:
                    status = "pending"
                class_cards.append({
                    'id':f"{entry.class_id.class_id}_{entry.subject_id.subject_id}_{entry.period}_{current_date}",
                    'class_id': entry.class_id.class_id,
                    'subject_id':entry.subject_id.subject_id,
                    'department_id': entry.subject_id.department_id.department_id,
                    'class_name':entry.class_id.class_name,
                    'semester':entry.subject_id.semester,
                    'date':current_date.strftime('%Y-%m-%d'),
                    'period':entry.period,
                    'status':status,
                    'students': class_student
                })
        current_date += timedelta(days=1)

    # === Result Entry Logic ===

    subject_handled = Class_Timetable.objects.filter(staff_id=staff.staff_id).values_list('subject_id','class_id').distinct()
    grade = Grade.objects.all().order_by('-min_percentage')
    results_entry_data = {}
    print(subject_handled)
    

    for subject_id, class_id in subject_handled:
        class_and_subject_exist_in_Marks = Marks.objects.filter(subject_id_id=subject_id, class_id_id=class_id).exists()
        if class_and_subject_exist_in_Marks:
            continue  # Skip if records already exist
        subject = Subjects.objects.get(subject_id=subject_id)
        class_info = Classes.objects.get(class_id=class_id)
        print(subject, class_info)
        students_in_class = Student.objects.filter(class_id=class_id).order_by('roll_no')
        print(students_in_class[0])
        results_entry_data[f"{class_id}_{subject_id}"] = {
            'subject': subject,
            'class_info': class_info,
            'students': students_in_class,
        }

    if request.method == "POST":
        form_type = request.POST.get("form_type")

        # --- Attendance Form ---
        if form_type == "attendance":
            form = Attendance_entry(request.POST)
            if form.is_valid():
                class_id = form.cleaned_data['class_id']
                subject_id = form.cleaned_data['subject_id']
                current_department_id = form.cleaned_data['department_id']
                current_date_date = form.cleaned_data['date']
                period = form.cleaned_data['period']

                present_dict = form.get_attendance_data()
                all_students = Student.objects.filter(class_id=class_id)

                for student in all_students:
                    is_present = str(student.roll_no) in present_dict
                    Attendance.objects.create(
                        class_id_id=class_id,
                        subject_id_id=subject_id,
                        staff_id=staff,
                        department_id_id=current_department_id,
                        date=current_date_date,
                        period=period,
                        roll_no=student,
                        status='Present' if is_present else 'Absent'
                    )
                print("Attendance records created")
                return redirect(reverse("staff:staff_dashboard", kwargs={'slug': staff.slug}))
            else:
                print("Attendance form errors:", form.errors.as_data())

        # --- Results Form ---
        elif form_type == "results":
            result_entry_form = ResultsEntryForm(request.POST)
            if result_entry_form.is_valid():
                class_id = result_entry_form.cleaned_data['class_id']
                subject_id = result_entry_form.cleaned_data['subject_id']
                current_department_id = result_entry_form.cleaned_data['department_id']
                current_semester = result_entry_form.cleaned_data['semester']

                results_dict = result_entry_form.get_results_data()
                for roll_no, marks_obtained in results_dict.items():
                    try:
                        student = Student.objects.get(roll_no=roll_no)
                        marks_obtained = float(marks_obtained)
                        grade_obtained = None
                        for g in grade:
                            if g.min_percentage <= marks_obtained <= g.max_percentage:
                                grade_obtained = g
                                break

                        Marks.objects.update_or_create(
                            roll_no=student,
                            subject_id_id=subject_id,
                            class_id_id=class_id,
                            department_id_id=current_department_id,
                            semester=current_semester,
                            defaults={
                                'marks_obtained': marks_obtained,
                                'grade_obtained': grade_obtained
                            }
                        )
                    except Student.DoesNotExist:
                        print(f"Student with roll no {roll_no} does not exist.")
                    except ValueError:
                        print(f"Invalid marks '{marks_obtained}' for roll no {roll_no}.")
                return redirect(reverse("staff:staff_dashboard", kwargs={'slug': staff.slug}))
            else:
                print("Results form errors:", result_entry_form.errors.as_data())
                
    return render(request, 'staff/staff_DB.html', {
        'staff': staff,
        'timetable': timetable,
        'show_section': show_section,
        'students_record': students_record,
        'class_cards': class_cards,
        'results_entry_data': results_entry_data,
        'grade': grade,
    })


def staff_profile(request,slug):
    staff = get_object_or_404(Staff, slug=slug)

    return render(request, 'staff/staff_profile.html',{
        'staff': staff
    })

def staff_login(request):
    form = StaffLoginForm()
    if request.method == 'POST':
        form = StaffLoginForm(request.POST)
        if form.is_valid():
            staff_id = form.cleaned_data['staff_id']
            password = form.cleaned_data['password']
            try:
                staff_login = Staff_Login.objects.get(staff_id = staff_id)
                if check_password(password, staff_login.password):
                    staff = Staff.objects.get(staff_id=staff_id)
                    request.session['staff_slug'] = staff.slug
                    return redirect(reverse('staff:staff_dashboard', kwargs={'slug': staff.slug}))
            except Staff_Login.DoesNotExist:
                return render(request, 'staff/staff_login.html', {
                    'form': form,
                    'error': "Invalid staff ID or password",
                    'current_year': datetime.now().year
                })
        return render(request, 'staff/staff_login.html', {'form': form, 'current_year': datetime.now().year})
    return render(request, 'staff/staff_login.html', {'form': form, 'current_year': datetime.now().year})

def staff_logout(request):
    logout(request)
    return redirect(reverse('staff:staff_login'))  # Redirect to the login page after logout

def student_profile_record(request, slug, student_slug):
    student = get_object_or_404(Student, slug=student_slug)
    get_semester = Subjects.objects.filter(semester=student.current_semester,department_id_id=student.department_id)
    
    subject_professors = []

    for sem in get_semester:
        subject_staff = Class_Timetable.objects.filter(department_id_id=student.department_id,
                                                       class_id_id = student.class_id,
                                                       subject_id = sem.subject_id).select_related("staff_id")
        
        if subject_staff:
            staff_name = subject_staff.first().staff_id.staff_name
        else:
            staff_name = "N/A"
        
        subject_professors.append({
            "subject_id": sem.subject_id,
            "subject_name": sem.subject_name,
            "credits": sem.credits,
            "professor": staff_name
        })

    return render(request, 'staff/student_detail_profile.html', {
        'student': student,
        'current_semester': subject_professors,
    })

def edit_student_profile(request, slug, student_slug):
    student = get_object_or_404(Student, slug=student_slug)
    classess = Classes.objects.filter(department_id=student.department_id)
    department = Department.objects.all()
    semesters = range(1, student.department_id.no_of_semesters + 1)
    if request.method == 'POST':
        form = EditStudentProfileForm(request.POST, request.FILES, instance=student)
        if form.is_valid():
            edit_student = form.save(commit=False)
            edit_student.slug = slugify(f"{edit_student.name}-{uuid4().hex[:6]}")
            edit_student.save()
            return redirect(reverse('staff:student_profile_record', args=[slug, student.slug]))
    else:
        form = EditStudentProfileForm(instance=student)
    return render(request, 'staff/edit_student_profile.html', {
        'student': student,
        'classes': classess,
        'department': department,
        'semesters': semesters,
        'form': form
    })