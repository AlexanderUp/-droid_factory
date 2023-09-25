from django.contrib import admin

from customers.models import Customer


class CustomerAdmin(admin.ModelAdmin):
    list_display = (
        'pk',
        'email',
    )


admin.site.register(Customer, CustomerAdmin)
