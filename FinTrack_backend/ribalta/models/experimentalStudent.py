from . import person, courseClass
from django.db import models

class ExperimentalStudent(person):
    experimental_classes = models.ManyToManyField(courseClass, on_delete = models.CASCADE)

    def __str__(self):
        return f"Experimental - {self.student.name}"