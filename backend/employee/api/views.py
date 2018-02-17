import time
from logging import getLogger

from django.contrib.auth.models import User, Group
from employee.api.serializers import UserSerializer, GroupSerializer
from employee.common.constants import LOGGER_NAME
from rest_framework import viewsets
from rest_framework.response import Response


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    log = getLogger(LOGGER_NAME)

    def list(self, request):

        # 何かの処理
        time.sleep(1)

        print("users, execute something.")

        # 何かの処理
        time.sleep(1)

        return Response()


class GroupViewSet(viewsets.ModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
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
