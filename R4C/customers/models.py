from django.db import models


class Customer(models.Model):
    email = models.EmailField(
        max_length=255,
        unique=True,
        verbose_name="email",
        help_text="email",
    )

    class Meta:
        verbose_name = "Customer"
        verbose_name_plural = "Customers"
        ordering = ("-pk",)

    def __str__(self):
        return f"Customer({self.email})"
