# from rest_framework import generics, status
# from rest_framework.response import Response
# from .models import Employee, Attendance
# from .serializers import EmployeeSerializer, AttendanceSerializer
# from .services import EmployeeService, AttendanceService
# from django.shortcuts import render, redirect
# from django.utils.timezone import now
# from .models import Employee, Attendance

# class EmployeeListCreateView(generics.ListCreateAPIView):
#     queryset = Employee.objects.all().order_by("-created_at")
#     serializer_class = EmployeeSerializer

#     def create(self, request, *args, **kwargs):
#         serializer = self.get_serializer(data=request.data)
#         # serializer.is_valid(raise_exception=True)
#         employee = EmployeeService.create_employee(serializer.validated_data)
#         return Response(EmployeeSerializer(employee).data, status=status.HTTP_201_CREATED)


# class EmployeeDeleteView(generics.DestroyAPIView):
#     queryset = Employee.objects.all()
#     serializer_class = EmployeeSerializer


# class AttendanceCreateView(generics.CreateAPIView):
#     serializer_class = AttendanceSerializer

#     def create(self, request, *args, **kwargs):
#         serializer = self.get_serializer(data=request.data)
#         # serializer.is_valid(raise_exception=True)
#         attendance = AttendanceService.mark_attendance(serializer.validated_data)
#         return Response(
#             AttendanceSerializer(attendance).data,
#             status=status.HTTP_201_CREATED
#         )


# class AttendanceListView(generics.ListAPIView):
#     serializer_class = AttendanceSerializer

#     def get_queryset(self):
#         employee_id = self.request.query_params.get("employee_id")
#         return Attendance.objects.filter(employee__employee_id=employee_id)





from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.renderers import TemplateHTMLRenderer
from .models import Employee, Attendance
# from django.utils.timezone import now
from datetime import datetime

class EmployeePageView(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = "employees.html"

    def get(self, request):
        employees = Employee.objects.all().order_by("-created_at")
        return Response({"employees": employees})

    def post(self, request):
        Employee.objects.create(
            employee_id=request.data.get("employee_id"),
            full_name=request.data.get("full_name"),
            email=request.data.get("email"),
            department=request.data.get("department"),
        )
        employees = Employee.objects.all()
        return Response({"employees": employees})


class AttendancePageView(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = "attendance.html"

    def get(self, request):
        employees = Employee.objects.all()
        attendances = Attendance.objects.all().order_by("-date")

        return Response({
            "employees": employees,
            "attendances": attendances
        })

    def post(self, request):
        Attendance.objects.create(
            employee_id=request.data.get("employee"),
            date=request.data.get("date"),
            status=request.data.get("status")
        )

        employees = Employee.objects.all()
        attendances = Attendance.objects.all()

        return Response({
            "employees": employees,
            "attendances": attendances
        })


class DashboardView(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = "dashboard.html"

    def get(self, request):
        today = datetime.now().date()
        total_employees = Employee.objects.count()
        today_present = Attendance.objects.filter(
            date=today, status="PRESENT"
        ).count()

        return Response({
            "total_employees": total_employees,
            "today_present": today_present,
            "today_absent": total_employees - today_present
        })


