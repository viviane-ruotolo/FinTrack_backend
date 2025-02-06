from . import course, experimentalStudent
from django.db import models

class CourseClass(models.Model):
    id = models.AutoField(primary_key=True)
    is_active = models.BooleanField(default=True)
    description = models.TextField()
    date = models.DateField()
    course = models.ForeignKey(course, on_delete= models.CASCADE)
    experimental_students = models.ManyToManyField(experimentalStudent, on_delete= models.CASCADE)
    
    #Buscar presença pela tabela attendance

    def __str__():
        return "f{self.course.description} - {self.date}"
    
    def fill_attendance_list(self):
        pass

    def insert_experimental_student(self, student: experimentalStudent):
        self.experimental_students.add(student)
        self.save()
        pass

    # CRUD Methods
    @classmethod
    def create_course_class(cls, **kwargs):
        return cls.objects.create(**kwargs)

    def update_course(self, **kwargs):
        for key, value in kwargs.items():
            setattr(self, key, value)
        self.save()
        return self

    def delete_course(self):
        self.is_active = False