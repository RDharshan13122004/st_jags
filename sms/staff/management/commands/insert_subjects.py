from django.core.management.base import BaseCommand
from staff.models import Subjects
import csv

class Command(BaseCommand):
    help = "userd to insert data"

    def handle(self, *args, **kwargs):

        with open("E:/Dharshan Personal/lap_desktop/lang and tools/pyvsc/faker/subject_data.csv","r") as f:
            read_data = csv.DictReader(f,fieldnames=["subject_id", "subject_name", "credits", "semester"])
            next(read_data)
            for row in read_data:
                if "BCA" in row["subject_id"]:
                    Subjects.objects.create(subject_id=row["subject_id"],subject_name=row["subject_name"],semester=row["semester"],credits=row["credits"],department_id_id="BCAGEN")
                if "BBA" in row["subject_id"]:
                    Subjects.objects.create(subject_id=row["subject_id"],subject_name=row["subject_name"],semester=row["semester"],credits=row["credits"],department_id_id="BBA")
                if "AERO" in row["subject_id"]:
                    Subjects.objects.create(subject_id=row["subject_id"],subject_name=row["subject_name"],semester=row["semester"],credits=row["credits"],department_id_id="AEROSP")
                if "MECH" in row["subject_id"]:
                    Subjects.objects.create(subject_id=row["subject_id"],subject_name=row["subject_name"],semester=row["semester"],credits=row["credits"],department_id_id="MECH")
                if "EEE" in row["subject_id"]:
                    Subjects.objects.create(subject_id=row["subject_id"],subject_name=row["subject_name"],semester=row["semester"],credits=row["credits"],department_id_id="EEE")
                if "ENGLIS" in row["subject_id"]:
                    Subjects.objects.create(subject_id=row["subject_id"],subject_name=row["subject_name"],semester=row["semester"],credits=row["credits"],department_id_id="ENGLIS")
                if "BSCMAT" in row["subject_id"]:
                    Subjects.objects.create(subject_id=row["subject_id"],subject_name=row["subject_name"],semester=row["semester"],credits=row["credits"],department_id_id="BSCMAT")
                if "BECSE" in row["subject_id"]:
                    Subjects.objects.create(subject_id=row["subject_id"],subject_name=row["subject_name"],semester=row["semester"],credits=row["credits"],department_id_id="BECSE") 
                
        self.stdout.write(self.style.SUCCESS("Completed inserting data!"))       