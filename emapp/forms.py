# emapp/forms.py

from django import forms
from .models import Employee, Attendance

class EmployeeForm(forms.ModelForm):
    """
    Form for creating and updating Employee instances.
    """
    class Meta:
        model = Employee
        fields = ['name', 'designation', 'department', 'date_of_joining']

class AttendanceForm(forms.ModelForm):
    """
    Form for creating and updating Attendance instances.
    """
    class Meta:
        model = Attendance
        fields = ['employee', 'date', 'is_present']
