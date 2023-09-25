from django.conf import settings
from django.db import models


class Customer(models.Model):
    email = models.EmailField(
        max_length=settings.CUSTOMER_EMAIL_MAX_LENGTH,
        unique=True,
        verbose_name='email',
        help_text='email',
    )

    class Meta:
        verbose_name = 'Customer'
        verbose_name_plural = 'Customers'
        ordering = ('-pk',)

    def __str__(self):
        return f'Customer({self.email})'
