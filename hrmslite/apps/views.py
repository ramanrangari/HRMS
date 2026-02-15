from rest_framework import generics, status
from rest_framework.response import Response
from .models import Employee, Attendance
from .serializers import EmployeeSerializer, AttendanceSerializer
from .services import EmployeeService, AttendanceService

class EmployeeListCreateView(generics.ListCreateAPIView):
    queryset = Employee.objects.all().order_by("-created_at")
    serializer_class = EmployeeSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        employee = EmployeeService.create_employee(serializer.validated_data)
        return Response(EmployeeSerializer(employee).data, status=status.HTTP_201_CREATED)


class EmployeeDeleteView(generics.DestroyAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer


class AttendanceCreateView(generics.CreateAPIView):
    serializer_class = AttendanceSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        attendance = AttendanceService.mark_attendance(serializer.validated_data)
        return Response(
            AttendanceSerializer(attendance).data,
            status=status.HTTP_201_CREATED
        )


class AttendanceListView(generics.ListAPIView):
    serializer_class = AttendanceSerializer

    def get_queryset(self):
        employee_id = self.request.query_params.get("employee_id")
        return Attendance.objects.filter(employee__employee_id=employee_id)
