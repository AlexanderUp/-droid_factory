from django.conf import settings
from django.core.mail import send_mail
from robots.models import Robot

from .models import Order

ROBOT_ASSIGNED_MESSAGE_TEMPLATE = """
Добрый день!
Поздравляем! Вы успешно заказали робота модели {model}, версии {version}.
"""

ROBOT_AVAILABLE_MESSAGE_TEMPLATE = """
Добрый день!
Недавно вы интересовались нашим роботом модели {model}, версии {version}.
Этот робот теперь в наличии. Если вам подходит этот вариант - пожалуйста, свяжитесь с нами.
"""

ROBOT_UNAVAILABLE_MESSAGE_TEMPLATE = """
Добрый день!
Недавно вы интересовались нашим роботом модели {model}, версии {version}.
К сожалению, такого робота в наличии.
Как только он появится в продаже, мы сразу известим вас!
"""


def send_mail_to_customer(instance: Order,
                          subject: str,
                          template: str) -> None:
    send_mail(
        subject=subject,
        message=template.format(
            model=instance.robot_version.model.model,
            version=instance.robot_version.version,
        ),
        from_email=settings.ADMIN_EMAIL,
        recipient_list=[instance.customer.email],
    )


def send_mail_robot_assigned(instance: Order) -> None:
    subject = "DROID FACTORY: Robot assined to your order!"
    template = ROBOT_ASSIGNED_MESSAGE_TEMPLATE
    send_mail_to_customer(instance, subject, template)


def send_mail_robot_unavailable(instance: Order) -> None:
    subject = "DROID FACTORY: Robot unavailable."
    template = ROBOT_UNAVAILABLE_MESSAGE_TEMPLATE
    send_mail_to_customer(instance, subject, template)


def send_mail_robot_available(robot: Robot, recipients: list[str]) -> None:
    subject = "DROID FACTORY: Robot available."
    template = ROBOT_AVAILABLE_MESSAGE_TEMPLATE
    send_mail(
        subject=subject,
        message=template.format(
            model=robot.version.model.model,
            version=robot.version.version,
        ),
        from_email=settings.ADMIN_EMAIL,
        recipient_list=recipients,
    )
