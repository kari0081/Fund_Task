
from django.db import models


class Tasks(models.Model):
    tasks = models.CharField(max_length=250)
    tasks_title = models.CharField(max_length=500)
    tasks_logo = models.FileField()

    def __str__(self):
        return self.tasks + ' - ' + self.tasks_title + ' - ' + self.tasks_logo


#class Student(models.Model):
 #   task - models.ForeignKey(Tasks, on_delete=models.CASCADE)