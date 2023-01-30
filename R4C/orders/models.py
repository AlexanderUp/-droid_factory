from django.db import models

from customers.models import Customer  # isort:skip
from robots.models import RobotVersion  # isort:skip


class Order(models.Model):
    customer = models.ForeignKey(
        Customer,
        on_delete=models.CASCADE,
        related_name="orders",
        verbose_name="customer",
        help_text="Order customer",
    )
    robot = models.ForeignKey(
        RobotVersion,
        on_delete=models.CASCADE,
        related_name="orders",
        verbose_name="robot",
        help_text="Version of ordered robot",
    )

    class Meta:
        verbose_name = "Order"
        verbose_name_plural = "Orders"
        ordering = ("-pk",)

    def __str__(self):
        return f"Order({self.customer.email}:{self.robot})"
