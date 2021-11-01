from django.db import models


class Department(models.Model):
    dept_name = models.CharField(max_length=200)
    dept_course = models.TextField()

    def __str__(self):
        return self.dept_name


class Student(models.Model):
    student_id = models.IntegerField(max_length=10)
    name = models.CharField(max_length=50)
    d_name = models.ForeignKey(Department, on_delete=models.CASCADE, related_name='dept')
    company_placed = models.CharField(max_length=50)
    year_graduated = models.IntegerField(max_length=6)


