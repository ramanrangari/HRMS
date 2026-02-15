from django.urls import path
from .views import  EmployeePageView, AttendancePageView, DashboardView

urlpatterns = [
    path("", DashboardView.as_view(), name="dashboard"),
    path("employees/", EmployeePageView.as_view(), name="employees"),
    path("attendance/", AttendancePageView.as_view(), name="attendance"),
]
