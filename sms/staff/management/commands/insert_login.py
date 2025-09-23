from django.core.management.base import BaseCommand
from staff.models import Staff_Login
from django.contrib.auth.hashers import make_password
import csv

class Command(BaseCommand):
    help = "insert login data of staffs"

    def handle(self, *args, **kwargs):
        Staff_Login.objects.all().delete()
        with open("E:/Dharshan Personal/lap_desktop/lang and tools/pyvsc/faker/staff_login.csv","r") as f:
            read_data = csv.DictReader(f,fieldnames=["staff_id", "password"])
            next(read_data)
            for row in read_data:
                hash_password = make_password(row["password"])
                Staff_Login.objects.create(staff_id_id=row["staff_id"],password=hash_password)

        self.stdout.write(self.style.SUCCESS("completed"))


