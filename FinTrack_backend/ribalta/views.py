#from django.http import HttpResponse
from rest_framework import viewsets
from .models import Student, Course, CourseClass, ExperimentalStudent, UserAdmin, Payment, Showcase, Attendance
from .serializers import BasicStudentSerializer, CourseSerializer, CourseClassSerializer, ExperimentalStudentSerializer, UserAdminSerializer, PaymentSerializer, ShowcaseSerializer, AttendanceSerializer


#def home(request):
#    return HttpResponse("Hello world!")

#ModelViewSet: Aplica todas as funções do CRUD automaticamente
class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = BasicStudentSerializer

class CourseViewSet(viewsets.ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer

class CourseClassViewSet(viewsets.ModelViewSet):
    queryset = CourseClass.objects.all()
    serializer_class = CourseClassSerializer

class ExperimentalStudentViewSet(viewsets.ModelViewSet):
    queryset = ExperimentalStudent.objects.all()
    serializer_class = ExperimentalStudentSerializer

class UserAdminViewSet(viewsets.ModelViewSet):
    queryset = UserAdmin.objects.all()
    serializer_class = UserAdminSerializer

class PaymentViewSet(viewsets.ModelViewSet):
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer

class ShowcaseViewSet(viewsets.ModelViewSet):
    queryset = Showcase.objects.all()
    serializer_class = ShowcaseSerializer

class AttendanceViewSet(viewsets.ModelViewSet):
    queryset = Attendance.objects.all()
    serializer_class = AttendanceSerializer