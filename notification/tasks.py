from celery import shared_task

from nerdvanapp.models import User
from notification.models import SentNotification
from django.core.mail import send_mail
from nerdvana import settings


@shared_task
def send_email(from_email, to_email, subject, message, user_id, reason):
    sent_notification = SentNotification.objects.create(
        recipient=User.objects.get(id=user_id),
        content=message,
        reason=reason
    )
    send_mail(
        subject=subject,
        message=message,
        from_email=from_email,
        recipient_list=[settings.EMAIL_RECIPIENT_ADDRESS, to_email]
    )
    sent_notification.set_sent()
