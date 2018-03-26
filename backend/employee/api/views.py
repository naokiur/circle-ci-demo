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


class UserViewSet(viewsets.ModelViewSet):
    queryset = Employee.objects.all()
    # queryset = User.objects.all().order_by('-date_joined')
    # serializer_class = UserSerializer

    def __init__(self):
        self.logger = getLogger(LOGGER_NAME)

    def list(self, request):

        # 何かの処理
        time.sleep(1)

        print("users, execute something.")

        # 何かの処理
        time.sleep(1)

        return Response()


class GroupViewSet(viewsets.ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = DummySerializer
    log = getLogger(LOGGER_NAME)

    def list(self, request):
        self.log.info("グループ取得機能開始")

        # 何かの処理
        time.sleep(1)

        print("groups, execute something.")

        # 何かの処理
        time.sleep(1)

        self.log.info("グループ取得機能終了")
        return Response()


class QuerySetConfirmViewSet(viewsets.ModelViewSet):
    queryset = Employee.objects.all()
    # serializer_class = GroupSerializer

    def __init__(self, **kwargs):
        super(QuerySetConfirmViewSet, self).__init__(**kwargs)
        self.logger = getLogger(LOGGER_NAME)

    def list(self, request):
        Employee.objects.create(
            user_id='123',
            password='admin',
            first_name='aaa',
            last_name='bbb',
            post_code='5',
            age=20,
            enter_date=datetime.today()
        )

        employee_query = Employee.objects.all()
        print(employee_query)

        [print(q) for q in employee_query]

        one_employee = employee_query[:1]
        print(one_employee)

        return Response()
