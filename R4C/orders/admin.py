from django.contrib import admin

from orders.models import Order


class OrderAdmin(admin.ModelAdmin):
    list_display = (
        'pk',
        'customer',
        'robot_version',
        'robot_assigned',
    )
    empty_value_display = '---empty---'
    fieldsets = (
        (
            None,
            {
                'fields': ('customer', 'robot_version'),
            },
        ),
    )


admin.site.register(Order, OrderAdmin)
