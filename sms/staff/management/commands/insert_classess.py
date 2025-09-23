from django.core.management.base import BaseCommand
from staff.models import Classes
import csv

class Command(BaseCommand):
    help = "insert classess Data"

    def handle(self, *args, **kwargs):
        with open("E:/Dharshan Personal/lap_desktop/lang and tools/pyvsc/faker/class_data.csv","r") as f:
            read_data = csv.DictReader(f, fieldnames=["class_id", "class_name","department_id"])
            next(read_data)
            for row in read_data:
                Classes.objects.create(
                    class_id=row["class_id"],
                    class_name=row["class_name"],
                    department_id_id=row["department_id"]
                )

        self.stdout.write(self.style.SUCCESS("Successfully inserted class data!"))