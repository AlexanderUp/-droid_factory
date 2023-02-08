from django.conf import settings
from django.core.mail import send_mail
from django.template import Context, Engine

from robots.models import Robot  # isort:skip
from .models import Order  # isort:skip


engine = Engine.get_default()


def send_mail_to_customer(instance: Order,
                          subject: str,
                          template_name: str,
                          engine: Engine = engine) -> None:
    template = engine.get_template(template_name=template_name)
    context = Context({
        "model": instance.robot_version.model.model,
        "version": instance.robot_version.version,
    })
    send_mail(
        subject=subject,
        message=template.render(context),
        from_email=settings.ADMIN_EMAIL,
        recipient_list=[instance.customer.email],
    )


def send_mail_robot_assigned(instance: Order) -> None:
    subject = "DROID FACTORY: Robot assined to your order!"
    template = "mail/robot_assigned.txt"
    send_mail_to_customer(instance, subject, template)


def send_mail_robot_unavailable(instance: Order) -> None:
    subject = "DROID FACTORY: Robot unavailable."
    template = "mail/robot_unavailable.txt"
    send_mail_to_customer(instance, subject, template)


def send_mail_robot_available(robot: Robot, recipients: list[str]) -> None:
    subject = "DROID FACTORY: Robot available."
    template = engine.get_template(
        template_name="mail/robot_available.txt")
    context = Context({
        "model": robot.version.model.model,
        "version": robot.version.version,
    })
    send_mail(
        subject=subject,
        message=template.render(context),
        from_email=settings.ADMIN_EMAIL,
        recipient_list=recipients,
    )
