from rest_framework import mixins, viewsets

from api.serializers import RobotWriteOnlySerializer
from robots.models import Robot


class RobotCreateViewSet(mixins.CreateModelMixin, viewsets.GenericViewSet):
    queryset = Robot.objects.all()
    serializer_class = RobotWriteOnlySerializer
