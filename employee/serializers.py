from rest_framework import serializers
from employee.models import Employee, LoginUser


class EmployeeSerializer(serializers.Serializer):

    def create(self, validated_data):
        return ''

    def update(self, instance, validated_data):
        return ''

    class Meta:
        model = Employee
        fields = ()


class LoginUserSerializer(serializers.Serializer):

    def update(self, instance, validated_data):
        pass

    def create(self, validated_data):
        pass

    class Meta:
        model = LoginUser
