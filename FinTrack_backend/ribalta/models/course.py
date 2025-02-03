from . import student, courseClass
from django.db import models


class Course(models.Model):
    id = models.AutoField(primary_key=True)
    is_active = models.BooleanField(default=True)
    description = models.CharField(max_length=255)
    value = models.FloatField()
    #Representar os dias de uma forma melhor -> enum?
    day_of_week = models.CharField(max_length=40)
    class_time = models.DurationField
    students = models.ManyToManyField(student, on_delete= models.CASCADE)
    #É ONE TO MANY - PRECISA ARRUMARRRR
    classes = models.OneToOneField(courseClass, on_delete= models.CASCADE)

    def __str__(self):
        return self.description
    
    # CRUD Methods
    @classmethod
    def create_course(cls, **kwargs):
        return cls.objects.create(**kwargs)

    def update_course(self, **kwargs):
        for key, value in kwargs.items():
            setattr(self, key, value)
        self.save()
        return self

    def delete_course(self):
        self.is_active = False

