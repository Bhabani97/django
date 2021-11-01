from django.contrib import admin
from .models import Department
from .models import Student


class AdminDepartment(admin.ModelAdmin):
    list_display = ['dept_name', 'dept_course']


class AdminStudent(admin.ModelAdmin):
    list_display = ['student_id', 'name', 'd_name', 'company_placed', 'year_graduated']


admin.site.register(Department, AdminDepartment)

admin.site.register(Student, AdminStudent)
