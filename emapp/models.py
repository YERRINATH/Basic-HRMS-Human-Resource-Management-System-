# emapp/models.py

from django.db import models
from django.utils import timezone

class Employee(models.Model):
    """
    Model representing an employee.
    """
    name = models.CharField(max_length=100)
    designation = models.CharField(max_length=50)
    department = models.CharField(max_length=50)
    date_of_joining = models.DateField()

    def __str__(self):
        return self.name

    def get_present_days(self):
        """
        Get a list of all present days for the employee.
        """
        return self.attendance_set.filter(is_present=True).values_list('date', flat=True)

class Attendance(models.Model):
    """
    Model representing attendance records for employees.
    """
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    date = models.DateField(default=timezone.now)
    is_present = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.employee.name} - {self.date} - {'Present' if self.is_present else 'Absent'}"
