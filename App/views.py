from django.shortcuts import render
from .models import Employee

# Create your views here.
def home(request):
    employee_list = Employee.objects.all()
    return render(request, 'home.html', {'employees': employee_list})