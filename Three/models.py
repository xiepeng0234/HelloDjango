from django.db import models

class Grade(models.Model):
    g_name = models.CharField(max_length=32)

class Student(models.Model):
    s_name = models.CharField(max_length=16)
    s_grad = models.ForeignKey(Grade)
