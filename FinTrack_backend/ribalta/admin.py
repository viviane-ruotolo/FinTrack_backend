from django.contrib import admin
from .models import Person, Student, Course, CourseClass, ExperimentalStudent, UserAdmin, Showcase, Attendance, Payment

admin.site.register(Student)
admin.site.register(Course)
admin.site.register(CourseClass)
admin.site.register(ExperimentalStudent)
admin.site.register(UserAdmin)
admin.site.register(Showcase)
admin.site.register(Attendance)
admin.site.register(Payment)
