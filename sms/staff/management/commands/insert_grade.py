from django.core.management.base import BaseCommand
from staff.models import Grade

class Command(BaseCommand):
    help = 'Insert predefined grades into the Grade model'

    def handle(self, *args, **kwargs):
        grades = [
            {'grade_name': 'A', 'min_percentage': 90, 'max_percentage': 100},
            {'grade_name': 'B', 'min_percentage': 80, 'max_percentage': 89},
            {'grade_name': 'C', 'min_percentage': 70, 'max_percentage': 79},
            {'grade_name': 'D', 'min_percentage': 60, 'max_percentage': 69},
            {'grade_name': 'E', 'min_percentage': 50, 'max_percentage': 59},
            {'grade_name': 'U', 'min_percentage': 0, 'max_percentage': 49},
        ]

        for grade_data in grades:
            grade, created = Grade.objects.get_or_create(
                grade_name=grade_data['grade_name'],
                defaults={
                    'min_percentage': grade_data['min_percentage'],
                    'max_percentage': grade_data['max_percentage']
                }
            )
            if created:
                self.stdout.write(self.style.SUCCESS(f"Inserted grade: {grade.grade_name}"))
            else:
                self.stdout.write(self.style.WARNING(f"Grade {grade.grade_name} already exists"))