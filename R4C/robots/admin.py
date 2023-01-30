from django.contrib import admin

from .models import Robot, RobotModel, RobotVersion


class RobotModelAdmin(admin.ModelAdmin):
    list_display = (
        "pk",
        "model",
    )


class RobotVersionAdmin(admin.ModelAdmin):
    list_display = (
        "pk",
        "model",
        "version",
        "robot_count",
    )

    def get_queryset(self, request):
        return super().get_queryset(request).prefetch_related("robots")

    @admin.display(description="robot_count")
    def robot_count(self, obj):
        return obj.robots.count()


class RobotAdmin(admin.ModelAdmin):
    list_display = (
        "pk",
        "serial",
        "robot_model",
        "created",
        "order",
    )
    list_select_related = (
        "version",
        "version__model",
        "order",
    )
    empty_value_display = "-----"

    @admin.display(description="robot_model")
    def robot_model(self, obj):
        return "-".join((obj.version.model.model, obj.version.version))


admin.site.register(RobotModel, RobotModelAdmin)
admin.site.register(RobotVersion, RobotVersionAdmin)
admin.site.register(Robot, RobotAdmin)
