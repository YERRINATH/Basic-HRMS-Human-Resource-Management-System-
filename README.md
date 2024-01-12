# HRMS Django App

This Django project simulates a basic Human Resource Management System (HRMS) with functionalities such as employee management, attendance tracking, and basic reporting.

## Project Overview

The project is structured with Django, and it includes the following components:

- **emapp:** Django app for employee management.
- **empro:** Django project settings and configuration.

## Getting Started

 Project Structure:
 
    ```bash
       empro/
        ├── emapp/
        │   ├── __init__.py
        │   ├── admin.py
        │   ├── apps.py
        │   ├── migrations/
        │   │   └── __init__.py
        │   ├── models.py
        │   ├── tests.py
        │   └── views.py
        |   |__ urls.py
        ├── empro/
        │   ├── __init__.py
        │   ├── asgi.py
        │   ├── settings.py
        │   ├── urls.py
        │   └── wsgi.py
        └── manage.py


1. Clone the repository:

   ```bash
   https://github.com/YERRINATH/Basic-HRMS-Human-Resource-Management-System-.git
2. Install dependencies:

   ```bash
   pip install -r requirements.txt
3. Apply migrations:

   ```bash
   python manage.py migrate
4. Run the development server:

   ```bash
   python manage.py runserver
# Functionalities

## Home Page

The home page ("/") welcomes users with a friendly message.
<img width="918" alt="home p" src="https://github.com/YERRINATH/Basic-HRMS-Human-Resource-Management-System-/assets/83647996/64b572ed-a6a3-4100-8a27-c0c8fdcbb8d4">


## Employee Management

- Database model for employees with attributes like name, designation, department, and date of joining.
- API endpoint to add a new employee (`/add_employee/`).
- API endpoint to retrieve the list of all employees (`/employees/`).
- Route to display the list of employees on the home page (`/`).
<img width="757" alt="add e p" src="https://github.com/YERRINATH/Basic-HRMS-Human-Resource-Management-System-/assets/83647996/53fd1398-781f-46cf-b202-43cd67ecafe2">


## Attendance Tracking

- Added fields for attendance in the employee model.
- API endpoint to mark attendance for a specific employee on a given date (`/mark_attendance/`).
- API endpoint to retrieve attendance details for a specific employee (`/attendance_details/{employee_id}/`).
- Display attendance details on the employee details page (`/employee_details/{employee_id}/`).
<img width="664" alt="g att" src="https://github.com/YERRINATH/Basic-HRMS-Human-Resource-Management-System-/assets/83647996/cdf1a632-992c-4939-9ae8-dd8d1606c6f3">
<img width="959" alt="att e p" src="https://github.com/YERRINATH/Basic-HRMS-Human-Resource-Management-System-/assets/83647996/add572a9-838a-4cb0-b933-fcfd8bcc141b">


## Django Admin

- Admin can view tables and manage data using the Django Admin interface (`/admin/`).
<img width="947" alt="image" src="https://github.com/YERRINATH/Basic-HRMS-Human-Resource-Management-System-/assets/83647996/aed1e055-063f-427c-b457-48792b847666">
<img width="938" alt="image" src="https://github.com/YERRINATH/Basic-HRMS-Human-Resource-Management-System-/assets/83647996/c4d3f081-a68c-4997-8dc4-734087f7c596">


Feel free to customize and expand upon this basic HRMS according to your specific requirements. Refer to the Django documentation for more details on Django project structure and application development: [Django Documentation](https://docs.djangoproject.com/).
   
