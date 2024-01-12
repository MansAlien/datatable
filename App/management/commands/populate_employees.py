# App/management/commands/populate_employees.py

from django.core.management.base import BaseCommand
from faker import Faker
from App.models import Employee
import random

class Command(BaseCommand):
    help = 'Populate the Employee table with 20 random entries'

    def handle(self, *args, **kwargs):
        fake = Faker()

        for _ in range(20):
            name = fake.name()
            email = fake.email()
            occupation = fake.job()
            salary = str(random.randint(30000, 120000))
            gender = random.choice(['M', 'F'])

            Employee.objects.create(
                name=name,
                email=email,
                occupation=occupation,
                salary=salary,
                gender=gender
            )

        self.stdout.write(self.style.SUCCESS('Successfully populated the Employee table with 20 random entries'))
