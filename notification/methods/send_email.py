from notification.tasks import send_email
from nerdvana import settings


class SendNotification:
    from_email = settings.EMAIL_HOST_USER

    @classmethod
    def send_email_proxy(cls, to_email, subject, message, user_id, reason):
        send_email.delay(
            from_email=cls.from_email,
            to_email=to_email,
            subject=subject,
            message=message,
            user_id=user_id,
            reason=reason
        )
