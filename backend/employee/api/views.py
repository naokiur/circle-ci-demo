from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from rest_framework.response import Response

from employee.api.serializers import UserSerializer, GroupSerializer
from employee.common.interceptor.logger import logger


class UserViewSet(viewsets.ModelViewSet):
	queryset = User.objects.all().order_by('-date_joined')
	serializer_class = UserSerializer

	@logger(func_name="ユーザ取得機能")
	def list(self, request):
		print("users")

		return Response()


class GroupViewSet(viewsets.ModelViewSet):
	queryset = Group.objects.all()
	serializer_class = GroupSerializer

	@logger(func_name="グループ取得機能")
	def list(self, request):
		print("groups")

		return Response()
