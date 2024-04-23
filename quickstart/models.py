from django.db import models


class Employee(models.Model):
    name = models.CharField(max_length=100)
    department = models.CharField(max_length=100)


class Profile(models.Model):
    employee = models.OneToOneField(Employee, on_delete=models.CASCADE)
    bio = models.TextField()
