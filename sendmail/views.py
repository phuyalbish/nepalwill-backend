from django.conf import settings
from django.core.mail import send_mail


def mailer(subject, message, to):
    send_mail(subject, message, settings.EMAIL_HOST_USER, to)


def consultation_message_received_mail(sender, message, htmessage):
    mailer(
        f"Inquiry Mmessage from {sender}",
        htmessage,
        ["mrvishope@gmail.com"],
    )
    mailer(
        f"Hey {sender}, from XYZ",
        message,
        [
            sender,
        ],
    )
