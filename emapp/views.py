# emapp/views.py

from django.shortcuts import render, get_object_or_404, redirect
from django.http import JsonResponse
from .models import Employee,Attendance
from .forms import EmployeeForm
from .forms import AttendanceForm
from django.contrib import messages

def take_attendance(request):
    """
    View for taking employee attendance. Handles both GET and POST requests.

    On a POST request, validates the submitted form, saves the attendance record, and redirects to the employee list view.
    On a GET request, renders the attendance form.

    :param request: HTTP request object
    :return: HTTP response object
    """
    if request.method == 'POST':
        form = AttendanceForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('get_all_employees')
    else:
        form = AttendanceForm()

    return render(request, 'take_attendance.html', {'form': form})

def index(request):
    """
    View for displaying a list of all employees.

    :param request: HTTP request object
    :return: HTTP response object
    """
    employees = Employee.objects.all()
    return render(request, 'index.html', {'employees': employees})


def add_employee(request):
    """
    View for adding a new employee. Handles both GET and POST requests.

    On a POST request, validates the submitted form, saves the employee record, and redirects to the index with a success message.
    On a GET request, renders the employee form.

    :param request: HTTP request object
    :return: HTTP response object
    """
    if request.method == 'POST':
        form = EmployeeForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Employee added successfully')
            return redirect('index')  # Replace 'index' with the actual name or URL of your index view
        else:
            messages.error(request, 'Invalid form data')

    elif request.method == 'GET':
        form = EmployeeForm()
        return render(request, 'add_employee.html', {'form': form})

    return JsonResponse({'error': 'Invalid request method'})



def get_all_employees(request):
    employees = Employee.objects.all()
    context = {'employees': employees}
    return render(request, 'employees_list.html', context)

def employee_detail_with_attendance(request, employee_id):
    """
    View for displaying employee details along with their present days.
    """
    employee = Employee.objects.get(pk=employee_id)
    present_days = employee.get_present_days()

    context = {
        'employee': employee,
        'present_days': present_days,
    }

    return render(request, 'employee_detail_with_attendance.html', context)

def attendance_list(request):
    attendance_records = Attendance.objects.all()
    return render(request, 'attendance_list.html', {'attendance_records': attendance_records})