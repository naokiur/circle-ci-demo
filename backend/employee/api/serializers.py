# from django.contrib.auth.models import User, Group
from rest_framework import serializers

#
# class UserSerializer(serializers.HyperlinkedModelSerializer):
#     class Meta:
#         model = User
#         fields = ('url', 'username', 'email', 'groups')
#
#
# class GroupSerializer(serializers.HyperlinkedModelSerializer):
#     class Meta:
#         model = Group
#         fields = ('url', 'name')
#
from employee.api.models import Employee, Login


class DummySerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = '__all__'


class LoginSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = ('user_id', 'password')

    def __init__(self, queryset):
        print(self.data)
        print(queryset)
