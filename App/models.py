from django.db import models

# Create your models here.
class Employee(models.Model):
    GENDER = (
        ('M','M'),
        ('F','F')
    )
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    email = models.EmailField()
    occupation = models.CharField(max_length=100)
    salary = models.CharField(max_length=100)
    gender = models.CharField(max_length=1, null=True, choices=GENDER)

    def __str__(self):
        return self.name