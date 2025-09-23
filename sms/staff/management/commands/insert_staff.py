from django.core.management.base import BaseCommand
from staff.models import Staff, Department
from django.utils.text import slugify
import csv
import uuid

class Command(BaseCommand):
    help = "inserting data"

    def handle(self, *args, **kwargs):

        Staff.objects.all().delete()
        
        with open("E:/Dharshan Personal/lap_desktop/lang and tools/pyvsc/faker/staff_data.csv","r") as f:
            read_data = csv.DictReader(f,fieldnames=["staff_id", 
                                             "name",
                                             "email", 
                                             "phone", 
                                             "address",
                                             "dob", 
                                             "gender",  
                                             "staff_designation"])
            
            next(read_data)
            for row in read_data:
                if "CSE" in row["staff_id"]:
                    Staff.objects.create(staff_id=row["staff_id"],
                                        staff_name=row["name"],
                                        staff_email=row["email"],
                                        staff_phone=int(row["phone"]),
                                        staff_address=row["address"],
                                        staff_DOB=row["dob"],
                                        gender=row["gender"],
                                        slug = slugify(f"{row['name']}-{uuid.uuid4().hex[:6]}"),
                                        staff_designation=row["staff_designation"],
                                        department_id_id="BECSE")

                    
                elif "EEE" in row["staff_id"]:
                    Staff.objects.create(staff_id=row["staff_id"],
                                        staff_name=row["name"],
                                        staff_email=row["email"],
                                        staff_phone=int(row["phone"]),
                                        staff_address=row["address"],
                                        staff_DOB=row["dob"],
                                        gender=row["gender"],
                                        slug = slugify(f"{row['name']}-{uuid.uuid4().hex[:6]}"),
                                        staff_designation=row["staff_designation"],
                                        department_id_id= "EEE")

                elif "BCA" in row["staff_id"]:
                    Staff.objects.create(staff_id=row["staff_id"],
                                        staff_name=row["name"],
                                        staff_email=row["email"],
                                        staff_phone=int(row["phone"]),
                                        staff_address=row["address"],
                                        staff_DOB=row["dob"],
                                        gender=row["gender"],
                                        slug = slugify(f"{row['name']}-{uuid.uuid4().hex[:6]}"),
                                        staff_designation=row["staff_designation"],
                                        department_id_id= "BCAGEN")

                elif "MECH" in row["staff_id"]:
                    Staff.objects.create(staff_id=row["staff_id"],
                                        staff_name=row["name"],
                                        staff_email=row["email"],
                                        staff_phone=int(row["phone"]),
                                        staff_address=row["address"],
                                        staff_DOB=row["dob"],
                                        gender=row["gender"],
                                        slug = slugify(f"{row['name']}-{uuid.uuid4().hex[:6]}"),
                                        staff_designation=row["staff_designation"],
                                        department_id_id= "MECH")

                elif "AERO" in row["staff_id"]:
                    Staff.objects.create(staff_id=row["staff_id"],
                                        staff_name=row["name"],
                                        staff_email=row["email"],
                                        staff_phone=int(row["phone"]),
                                        staff_address=row["address"],
                                        staff_DOB=row["dob"],
                                        gender=row["gender"],
                                        slug = slugify(f"{row['name']}-{uuid.uuid4().hex[:6]}"),
                                        staff_designation=row["staff_designation"],
                                        department_id_id= "AEROSP")

                elif "BSCM" in row["staff_id"]:
                    Staff.objects.create(staff_id=row["staff_id"],
                                        staff_name=row["name"],
                                        staff_email=row["email"],
                                        staff_phone=int(row["phone"]),
                                        staff_address=row["address"],
                                        staff_DOB=row["dob"],
                                        gender=row["gender"],
                                        slug = slugify(f"{row['name']}-{uuid.uuid4().hex[:6]}"),
                                        staff_designation=row["staff_designation"],
                                        department_id_id= "BSCMAT")

                elif "ENG" in row["staff_id"]:
                    Staff.objects.create(staff_id=row["staff_id"],
                                        staff_name=row["name"],
                                        staff_email=row["email"],
                                        staff_phone=int(row["phone"]),
                                        staff_address=row["address"],
                                        staff_DOB=row["dob"],
                                        gender=row["gender"],
                                        slug = slugify(f"{row['name']}-{uuid.uuid4().hex[:6]}"),
                                        staff_designation=row["staff_designation"],
                                        department_id_id= "ENGLIS")

                elif "BAA" in row["staff_id"]:
                    Staff.objects.create(staff_id=row["staff_id"],
                                        staff_name=row["name"],
                                        staff_email=row["email"],
                                        staff_phone=int(row["phone"]),
                                        staff_address=row["address"],
                                        staff_DOB=row["dob"],
                                        gender=row["gender"],
                                        slug = slugify(f"{row['name']}-{uuid.uuid4().hex[:6]}"),
                                        staff_designation=row["staff_designation"],
                                        department_id_id= "BBA")                    
            self.stdout.write(self.style.SUCCESS("successfully inserted"))
        