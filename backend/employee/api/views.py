import time
from logging import getLogger

from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from rest_framework.response import Response

from employee.api.serializers import UserSerializer, GroupSerializer
from employee.common.constants import LOGGER_NAME


class Dog:
	def __init__(self, name):
		self.name = name


class Cat:
	def __init__(self, name):
		self.name = name


class UserViewSet(viewsets.ModelViewSet):
	queryset = User.objects.all().order_by('-date_joined')
	serializer_class = UserSerializer
	log = getLogger(LOGGER_NAME)

	def list(self, request):
		self.log.info("ユーザ取得機能開始")

		dog_list = [
			Dog("A"),
			Dog("B"),
			Dog("C"),
			Dog("D"),
			Dog("E"),
		]

		cat_list = [
			Cat("A"),
			Cat("B"),
			Cat("C"),
			Cat("D"),
			Cat("E"),
		]

		# 何かの処理
		time.sleep(1)

		print("users, execute something.")
		print([x.name for x in dog_list])
		print([x.name for x in cat_list])

		# 何かの処理
		time.sleep(1)

		self.log.info("ユーザ取得機能終了")
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
