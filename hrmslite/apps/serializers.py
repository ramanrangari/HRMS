from rest_framework import serializers
from .models import Employee, Attendance

class EmployeeSerializer(serializers.ModelSerializer):

    class Meta:
        model = Employee
        fields = "__all__"

    def validate_employee_id(self, value):
        if Employee.objects.filter(employee_id=value).exists():
            raise serializers.ValidationError("Employee ID already exists.")
        return value

    def validate_email(self, value):
        if Employee.objects.filter(email=value).exists():
            raise serializers.ValidationError("Email already exists.")
        return value




class AttendanceSerializer(serializers.ModelSerializer):

    class Meta:
        model = Attendance
        fields = "__all__"

    def validate(self, attrs):
        employee = attrs.get("employee")
        date = attrs.get("date")

        if not Employee.objects.filter(id=employee.id).exists():
            raise serializers.ValidationError("Employee does not exist.")

        if Attendance.objects.filter(employee=employee, date=date).exists():
            raise serializers.ValidationError("Attendance already marked for this date.")

        return attrs
