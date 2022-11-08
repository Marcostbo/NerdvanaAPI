from django.db import models
from notification.constants import EMAIL_REASON


class SentNotification(models.Model):
    recipient = models.ForeignKey('nerdvanapp.User', on_delete=models.CASCADE)
    content = models.TextField(blank=True, null=True)
    reason = models.CharField(max_length=20, null=True, choices=EMAIL_REASON)
    sent = models.BooleanField(default=False)

    class Meta:
        verbose_name = 'Sent Notification'
        verbose_name_plural = 'Sent Notifications'

    def set_sent(self):
        self.sent = True
        self.save(update_fields=['sent'])

    def __str__(self):
        return f'{self.reason} - {self.recipient.email}'
