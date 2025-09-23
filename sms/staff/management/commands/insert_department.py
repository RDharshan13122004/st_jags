from django.core.management.base import BaseCommand
from staff.models import Department
import csv

class Command(BaseCommand):
    help = "insert base data"

    def handle(self, *args, **kwargs):
        Department.objects.all().delete()
        with open("E:/Dharshan Personal/lap_desktop/lang and tools/pyvsc/faker/department_data.csv", "r") as f:
            read_data = csv.DictReader(f,fieldnames=["depart_id", "depart_name","no_of_semesters"])
            next(read_data)
            #print([read_data["depart_id"]])
            for row in read_data:
                Department.objects.create(department_id=row["depart_id"],department_name=row["depart_name"],no_of_semesters=int(row["no_of_semesters"]))

        self.stdout.write(self.style.SUCCESS("completed inserting data!"))    