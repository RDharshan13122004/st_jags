from django.core.management.base import BaseCommand
from student.models import Student_Login
import csv
from django.contrib.auth.hashers import make_password

class Command(BaseCommand):
    help=""

    def handle(self, *args, **kwargs):
        Student_Login.objects.all().delete()
        with open("E:/Dharshan Personal/lap_desktop/lang and tools/pyvsc/faker/student_login.csv","r") as f:
            read_data = csv.DictReader(f,fieldnames=["roll_no", "password"])
            next(read_data)
            for row in read_data:
                hash_pwd=make_password(row["password"])
                Student_Login.objects.create(roll_no_id=row["roll_no"],
                                        password = hash_pwd)
                
            self.stdout.write(self.style.SUCCESS("completed"))