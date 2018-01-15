from django.db import models
from django.contrib.auth.models import User


class Employee(models.Model):
    emp_id = models.AutoField(
        primary_key=True)  # This will indicate a integer column 'emp_id' in Payroll table. and it is a primary key and auto incremented
    y = models.IntegerField()
    name = models.CharField(max_length=40)
    createdBy = models.ForeignKey(User,
                                  related_name="emp_create_user_fk", on_delete=models.CASCADE)

    createdTime = models.DateTimeField(auto_now_add=True)
    updatedBy = models.ForeignKey(User,
                                  related_name="emp_update_user_fk", on_delete=models.CASCADE)
    updatedTime = models.DateTimeField(auto_now_add=True)


class Salary(models.Model):
    sal_id = models.AutoField(primary_key=True)
    amount = models.DecimalField(max_digits=10, decimal_places=2,
                                 default=0)  # Here we create the decimal field which hold the salary. Max lenght is 10 and decimal 2
    createdBy = models.ForeignKey(User,
                                  related_name="sal_create_user_fk", on_delete=models.CASCADE)

    createdTime = models.DateTimeField(auto_now_add=True)
    updatedBy = models.ForeignKey(User,
                                  related_name="sal_update_user_fk", on_delete=models.CASCADE)

    updatedTime = models.DateTimeField(auto_now_add=True)
    emp_id = models.ForeignKey(Employee, related_name="sal_emp_id_fk", on_delete=models.CASCADE)


class Module(object):

    def __init__(self, moduleName, pin):
        self.moduleName = moduleName
        self.pin = pin
