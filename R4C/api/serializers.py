from django.utils import timezone
from rest_framework import serializers

from robots.models import Robot, RobotModel, RobotVersion


class RobotWriteOnlySerializer(serializers.Serializer):
    model = serializers.SlugField(max_length=2)
    version = serializers.SlugField(max_length=2)
    created = serializers.DateTimeField()

    def validate_model(self, value):
        if not RobotModel.objects.filter(model__iexact=value).exists():
            raise serializers.ValidationError('No such model!')
        return value.upper()

    def validate_version(self, value):
        return value.upper()

    def validate_created(self, value):
        if value > timezone.now():
            raise serializers.ValidationError(
                'Robot can not be created in future!',
            )
        return value

    def validate(self, data):
        model = RobotModel.objects.get(model=data['model'])
        robot_version_query = RobotVersion.objects.filter(
            model=model,
            version=data['version'],
        )
        if not robot_version_query.exists():
            raise serializers.ValidationError(
                'No model with specified version in database!',
            )
        return data

    def create(self, validated_data):
        model = RobotModel.objects.get(model=validated_data['model'])
        version = RobotVersion.objects.get(
            model=model,
            version=validated_data['version'],
        )
        created = validated_data['created']
        return Robot.objects.create(version=version, created=created)
