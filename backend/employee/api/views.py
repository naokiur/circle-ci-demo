import time
from datetime import datetime
from logging import getLogger

# from django.contrib.auth.models import User, Group
from rest_framework.views import APIView

from employee.api.models import Employee, Login
# from employee.api.serializers import UserSerializer, GroupSerializer
from employee.api.serializers import DummySerializer, LoginSerializer
from employee.common.constants import LOGGER_NAME
from rest_framework import viewsets
from rest_framework.response import Response


class LoginViewSet(APIView):

    def __init__(self):
        self.logger = getLogger(LOGGER_NAME)

    def get(self, request, format=None):
        self.logger.info('get method')
        queryset = Login.objects.all()
        self.logger.info(queryset)
        # serializer = LoginSerializer(queryset)

        # return Response(serializer.data)
        return Response()
