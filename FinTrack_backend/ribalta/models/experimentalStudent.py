from .person import Person
from django.db import models

class ExperimentalStudent(Person):
    experimental_classes = models.ManyToManyField('CourseClass')

    def __str__(self):
        return f"Experimental - {self.student.name}"