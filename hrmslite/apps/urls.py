from django.urls import path
from .views import  EmployeePageView, AttendancePageView

urlpatterns = [
    path("employees/", EmployeePageView.as_view(), name="employees"),
    path("attendance/", AttendancePageView.as_view(), name="attendance"),
]
