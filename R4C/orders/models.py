from django.core.exceptions import ValidationError
from django.db import models

from customers.models import Customer
from robots.models import Robot, RobotVersion


class Order(models.Model):
    customer = models.ForeignKey(
        Customer,
        on_delete=models.CASCADE,
        related_name='orders',
        verbose_name='customer',
        help_text='Order customer',
    )
    robot_version = models.ForeignKey(
        RobotVersion,
        on_delete=models.CASCADE,
        related_name='orders',
        verbose_name='robot',
        help_text='Version of ordered robot',
    )
    robot_assigned = models.OneToOneField(
        Robot,
        on_delete=models.SET_NULL,
        related_name='order',
        verbose_name='robot_assigned',
        help_text='Robot assigned to this order',
        null=True,
        blank=True,
    )

    class Meta:
        verbose_name = 'Order'
        verbose_name_plural = 'Orders'
        ordering = ('-pk',)

    def __str__(self):
        return 'Order({0}:{1})'.format(self.customer.email, self.robot_version)

    def clean(self):
        if self.robot_assigned:
            if self.robot_assigned.version != self.robot_version:
                raise ValidationError(
                    'Robot of requested version should be assigned!',
                )
