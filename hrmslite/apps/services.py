from .models import Employee, Attendance

class EmployeeService:

    @staticmethod
    def create_employee(data):
        return Employee.objects.create(**data)

    @staticmethod
    def delete_employee(employee_id):
        employee = Employee.objects.filter(id=employee_id).first()
        if not employee:
            return None
        employee.delete()
        return True

class AttendanceService:

    @staticmethod
    def mark_attendance(data):
        return Attendance.objects.create(**data)