from django.db import models

class Attendance(models.Model):
    course_class = models.ForeignKey('CourseClass', on_delete=models.CASCADE)
    student = models.ForeignKey('Student', on_delete=models.CASCADE)
    status = models.CharField(max_length=10, choices=[("PRESENT", "Presente"), ("ABSENT", "Ausente")])
    timestamp = models.DateTimeField(auto_now_add=True)  # Marca o horário da presença

    def __str__(self):
        return f"{self.student.name} - {self.course_class.description} ({self.status})"

