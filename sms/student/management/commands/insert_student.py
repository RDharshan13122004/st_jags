from django.core.management.base import BaseCommand
from student.models import Student
from django.utils.text import slugify
import csv
import uuid

class Command(BaseCommand):
    help = "inserting student datas"

    def handle(self, *args, **kwargs):
        Student.objects.all().delete()
        with open("E:/Dharshan Personal/lap_desktop/lang and tools/pyvsc/faker/student_data.csv","r") as f:
            read_data = csv.DictReader(f,fieldnames=["roll_no", 
                                            "name",
                                            "Father_name",
                                            "Mother_name",
                                            "dob",
                                            "gender",
                                            "email",
                                            "phone",
                                            "address",
                                            "school_name_10th",
                                            "school_name_12th",
                                            "marks_10th",
                                            "marks_12th",])
            
            next(read_data)
            for row in read_data:
                Student.objects.create(roll_no=row["roll_no"],
                                       name=row["name"],
                                       father_name=row["Father_name"],
                                       mother_name=row["Mother_name"],
                                       Dob = row["dob"],
                                       gender = row["gender"],
                                       email= row["email"],
                                       phone=row["phone"],
                                       address=row["address"],
                                       Education_10th=row["school_name_10th"],
                                       Education_12th=row["school_name_12th"],
                                       marks_10th=row["marks_10th"],
                                       marks_12th=row["marks_12th"],
                                       slug=slugify(f"{row['name']} + {uuid.uuid4().hex[:6]}")
                                       )
            
            self.stdout.write(self.style.SUCCESS("successfully inserted"))
