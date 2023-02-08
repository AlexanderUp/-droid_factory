from django.contrib import admin

from .models import Order


class OrderAdmin(admin.ModelAdmin):
    list_display = (
        "pk",
        "customer",
        "robot_version",
        "robot_assigned",
    )
    empty_value_display = "-----"
    fieldsets = (
        (
            None, {
                "fields": ("customer", "robot_version",),
            },
        ),
    )


admin.site.register(Order, OrderAdmin)
