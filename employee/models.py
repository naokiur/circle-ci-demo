from django.db import models

from django.db import models


class Employee(models.Model):

    family_name = models.CharField(max_length=20)
    first_name = models.CharField(max_length=20)
    post_code = models.CharField(max_length=2)
    updated_user = models.CharField(max_length=20)
    updated_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('updated_date',)


class LoginUser(models.Model):

    login_user_id = models.CharField(max_length=20)
    password = models.CharField(max_length=255)
