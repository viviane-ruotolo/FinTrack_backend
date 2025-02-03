from . import student
from django.db import models

class Showcase():
    id = models.AutoField(primary_key=True)
    description = models.CharField(max_length=255)
    date = models.DateField()
    student_cast = models.ManyToManyField(student, on_delete= models.CASCADE)
    expenses = models.JSONField(default=list)
    budgets = models.JSONField(default=list)
    final_cost = models.FloatField()

    def __str__(self):
        return f"{self.description} - {self.date}"
    
    def calculate_final_cost(self):
        for budget in self.budgets:
            self.final_cost += budget
        for expense in self.expenses:
            self.final_cost -= expense
        self.save()