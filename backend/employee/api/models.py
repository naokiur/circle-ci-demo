from django.db import models


class Employee(models.Model):
    user_id = models.CharField(max_length=12)
    password = models.TextField()
    first_name = models.TextField()
    last_name = models.TextField()
    post_code = models.CharField(max_length=10)
    age = models.IntegerField()
    enter_date = models.DateField()

    class Meta:
        managed = True
        db_table = 'employee'
