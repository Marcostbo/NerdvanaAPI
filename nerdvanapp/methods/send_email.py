from django.core.mail import send_mail
from nerdvana import settings


class SendNotification:
    from_email = settings.EMAIL_HOST_USER

    def send_email(self, to_email):
        send_mail(
            subject='Email do Django',
            message='Oi bolinho. Peo meleca',
            from_email=self.from_email,
            recipient_list=[settings.EMAIL_RECIPIENT_ADDRESS, to_email]
        )


notification = SendNotification()
notification.send_email(
    to_email='elisa.oliveira@engenharia.ufjf.br'
)
