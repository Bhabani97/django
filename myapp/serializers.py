from rest_framework import serializers
from .models import Department, Student


class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = '__all__'


class DepartmentSerializer(serializers.ModelSerializer):
    dept = StudentSerializer(many=True, read_only=True)

    class Meta:
        model = Department
        fields = '__all__'
