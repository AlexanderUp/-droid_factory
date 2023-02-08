from rest_framework import mixins, viewsets

from robots.models import Robot  # isort:skip
from .serializers import RobotWriteOnlySerializer  # isort:skip


class RobotCreateViewSet(mixins.CreateModelMixin,
                         viewsets.GenericViewSet):
    queryset = Robot.objects.all()
    serializer_class = RobotWriteOnlySerializer
