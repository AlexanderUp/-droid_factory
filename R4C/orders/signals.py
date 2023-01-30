from django.db.models.signals import post_save
from django.dispatch import receiver

from robots.models import Robot  # isort:skip
from .models import Order  # isort:skip
from .utils import (send_mail_robot_assigned,  # isort:skip
                    send_mail_robot_available,  # isort:skip
                    send_mail_robot_unavailable)  # isort:skip


@receiver(post_save, sender=Robot, dispatch_uid="robot_available_mail")
def robot_available_mail(sender, instance, created, **kwargs):
    if created:
        query = Order.objects.filter(
            robot_version=instance.version,
            robot_assigned__isnull=True,
        )
        if query.exists():
            recipients = set(query.values_list("customer__email", flat=True))
            send_mail_robot_available(instance, recipients)  # type:ignore


@receiver(post_save, sender=Order, dispatch_uid="order_done_mail")
def order_done_mail(sender, instance, created, **kwargs):
    if created:
        if instance.robot_assigned is None:
            query = instance.robot_version.robots.filter(
                order__isnull=True
            )
            if not query.exists():
                send_mail_robot_unavailable(instance)
                return None  # noqa
            robot = query.order_by("created")[0]
            instance.robot_assigned = robot
            instance.save()
        send_mail_robot_assigned(instance)
    return None  # noqa
