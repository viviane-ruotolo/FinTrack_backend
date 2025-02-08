from rest_framework import serializers
from .models import Student, Course, CourseClass, ExperimentalStudent, UserAdmin, Attendance, Payment, Showcase

class BasicStudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ['is_active', 'cpf', 'name', 'birth_date', 'email', 'address', 'telephone', 'total_value', 'discount', 'due_date']

class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = '__all__'

class AddStudentToCourse(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = 'students'

class CourseClassSerializer(serializers.ModelSerializer):
    class Meta:
        model = CourseClass
        fields = '__all__'

class ExperimentalStudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = ExperimentalStudent
        fields = '__all__'

class UserAdminSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserAdmin
        fields = '__all__'

class AttendanceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Attendance
        fields = '__all__'

class PaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payment
        fields = '__all__'

class ShowcaseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Showcase
        fields = '__all__'