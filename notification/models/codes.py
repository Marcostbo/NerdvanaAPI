from django.db import models
from notification.constants import EMAIL_REASON


class BaseCode(models.Model):
    user = models.ForeignKey('nerdvanapp.User', on_delete=models.CASCADE)
    code = models.IntegerField(max_length=6)
    creation_date = models.DateTimeField()
    reason = models.CharField(max_length=20, null=True, choices=EMAIL_REASON)

    class Meta:
        abstract = True


class PasswordRecoveryCode(BaseCode):

    class Meta:
        verbose_name = 'Password Recovery Code'
        verbose_name_plural = 'Password Recovery Codes'


class ValidateEmailCode(BaseCode):

    class Meta:
        verbose_name = 'Validate E-mail Code'
        verbose_name_plural = 'Validate E-mail Codes'
