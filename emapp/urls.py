# emapp/urls.py

from django.urls import path
from .views import take_attendance, index, add_employee, get_all_employees,employee_detail_with_attendance,attendance_list

urlpatterns = [
    path('', index, name='index'),
    path('add_employee/', add_employee, name='add_employee'),
    path('get_all_employees/', get_all_employees, name='get_all_employees'),
    path('take-attendance/', take_attendance, name='take_attendance'),
    path('employee/<int:employee_id>/', employee_detail_with_attendance, name='employee_detail_with_attendance'),
    path('attendance/', attendance_list, name='attendance_list'),
]
