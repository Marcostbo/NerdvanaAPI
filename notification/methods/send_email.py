from django.core.mail import send_mail
from nerdvana import settings


class SendNotification:
    from_email = settings.EMAIL_HOST_USER

    def send_email(self, to_email, subject, message):
        send_mail(
            subject=subject,
            message=message,
            from_email=self.from_email,
            recipient_list=[settings.EMAIL_RECIPIENT_ADDRESS, to_email]
        )
