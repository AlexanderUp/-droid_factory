from django.contrib import admin

from .models import Order


class OrderAdmin(admin.ModelAdmin):
    list_display = (
        "pk",
        "customer",
        "robot",
    )


admin.site.register(Order, OrderAdmin)
