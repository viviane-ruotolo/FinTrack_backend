from . import person, course, showcase
from django.db import models

class Student(person):
    total_value = models.FloatField()
    discount = models.FloatField()
    due_date = models.DateField()
    courses = models.ManyToManyField(course, on_delete = models.CASCADE)
    showcases = models.ManyToManyField(showcase, on_delete= models.CASCADE)

    def __str__(self):
        return f"{self.name} (Student)"
    
    #Discount applied in total_value
    def calculate_total_value(self):
        value_sum = 0
        for course in self.courses:
            value_sum += course.value 
        
        self.total_value = value_sum * (1 - self.discount)
        self.save()

