from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import StudentViewSet, CourseViewSet, CourseClassViewSet, ExperimentalStudentViewSet, UserAdminViewSet, ShowcaseViewSet, PaymentViewSet, AttendanceViewSet

router = DefaultRouter()
router.register(r'students', StudentViewSet)
router.register(r'courses', CourseViewSet)
router.register(r'course_classes', CourseClassViewSet)
router.register(r'experimental_students', ExperimentalStudentViewSet)
router.register(r'user_admins', UserAdminViewSet)
router.register(r'showcases', ShowcaseViewSet)
router.register(r'attendances', AttendanceViewSet)
router.register(r'payments', PaymentViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
