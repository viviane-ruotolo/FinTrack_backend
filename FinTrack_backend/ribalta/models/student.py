from .person import Person
from django.db import models

class Student(Person):
    total_value = models.FloatField()
    discount = models.FloatField()
    due_date = models.DateField()
    courses = models.ManyToManyField('Course')
    showcases = models.ManyToManyField('Showcase')

    def __str__(self):
        return f"{self.name} (Student)"
    
    #Discount applied in total_value
    def calculate_total_value(self):
        value_sum = 0
        for course in self.courses:
            value_sum += course.value 
        
        self.total_value = value_sum * (1 - self.discount)
        self.save()

