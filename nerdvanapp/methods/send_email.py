from django.core.mail import send_mail
from nerdvana import settings


class SendNotification:
    from_email = settings.EMAIL_HOST_USER

    def send_email(self, recipient):
        send_mail(
            subject='Email de teste',
            message='Oi bolinho',
            from_email=self.from_email,
            recipient_list=['oliveira.marcos@engenharia.ufjf.br', 'elisa.oliveira@engenharia.ufjf.br']
        )


notification = SendNotification()
notification.send_email(recipient=None)
