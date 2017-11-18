from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets

from employee.models import Employee, LoginUser
from employee.serializers import EmployeeSerializer, LoginUserSerializer


class EmployeeViewSet(viewsets.ModelViewSet):
    serializer_class = EmployeeSerializer
    queryset = Employee.objects.all()

    def get(self, request):
        pass

    def post(self, request):
        pass


class LoginUserViewSet(viewsets.ModelViewSet):
    serializer_class = LoginUserSerializer
    queryset = LoginUser.objects.all()

    def get(self, request):
        pass

    def post(self, request):
        pass
