import time
from datetime import datetime
from logging import getLogger

# from django.contrib.auth.models import User, Group
from rest_framework.views import APIView

from employee.api.models import Employee
# from employee.api.serializers import UserSerializer, GroupSerializer
from employee.api.serializers import DummySerializer, LoginSerializer
from employee.common.constants import LOGGER_NAME
from rest_framework import viewsets
from rest_framework.response import Response


class LoginViewSet(viewsets.GenericViewSet):
    queryset = Employee.objects.all()
    serializer_class = LoginSerializer

    def __init__(self):
        self.logger = getLogger(LOGGER_NAME)

    def create(self, request):
        print(request.param)
        self.logger.info(request.param)
        # serializer = LoginSerializer(self.queryset)

        # Employee.objects.filter(user_id=)

        return Response()
