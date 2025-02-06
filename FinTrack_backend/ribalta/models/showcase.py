from .student import Student
from django.db import models

class Showcase(models.Model):
    id = models.AutoField(primary_key=True)
    description = models.CharField(max_length=255)
    date = models.DateField()
    student_cast = models.ManyToManyField('Student')
    expenses = models.JSONField(default=list)
    budgets = models.JSONField(default=list)
    final_cost = models.FloatField()

    def __str__(self):
        return f"{self.description} - {self.date}"
    
    #Testar se esse cálculo realmente funciona
    def calculate_final_cost(self):
        for budget in self.budgets:
            self.final_cost += budget
        for expense in self.expenses:
            self.final_cost -= expense
        self.save()

    def add_student_to_cast(self, student: Student):
        self.student_cast.add(Student)
        self.save()