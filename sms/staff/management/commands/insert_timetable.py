from django.core.management.base import BaseCommand
from staff.models import Class_Timetable
import csv

class Command(BaseCommand):
    help = "Insert class timetable data from CSV file"
    def handle(self, *args, **kwargs):
        #Class_Timetable.objects.all().delete()
        with open("E:/Dharshan Personal/lap_desktop/lang and tools/pyvsc/faker/timetable_data.csv", "r") as f:
            read_data = csv.DictReader(f, fieldnames=["class_id", "staff_id", "subject_id", "department_id", "day", "period"])
            next(read_data)

            for row in read_data:
                Class_Timetable.objects.create(
                    class_id_id=row["class_id"],
                    staff_id_id=row["staff_id"],
                    subject_id_id=row["subject_id"],
                    department_id_id=row["department_id"],
                    day=row["day"],
                    period=int(row["period"])
                )
        self.stdout.write(self.style.SUCCESS("Completed inserting class timetable data!"))
        