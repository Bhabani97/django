from myapp.viewsets import StudentViewSet, DepartmentViewSet
from rest_framework import routers

router = routers.DefaultRouter()
router.register('student', StudentViewSet)
router.register('department', DepartmentViewSet)

