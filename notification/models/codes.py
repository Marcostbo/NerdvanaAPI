from django.db import models
from notification.constants import CODE_REASON, EMAIL_VALIDATION_VALID_TIME, PASSWORD_RECOVERY_VALID_TIME
from datetime import datetime, timedelta
from django.utils import timezone


class BaseCode(models.Model):
    user = models.ForeignKey('nerdvanapp.User', on_delete=models.CASCADE)
    code = models.IntegerField(max_length=6)
    creation_date = models.DateTimeField()
    reason = models.CharField(max_length=20, null=True, choices=CODE_REASON)
    validated = models.BooleanField(default=False, null=True, verbose_name='Code was validated?')

    class Meta:
        abstract = True


class PasswordRecoveryCode(BaseCode):

    class Meta:
        verbose_name = 'Password Recovery Code'
        verbose_name_plural = 'Password Recovery Codes'

    @property
    def is_valid(self):
        time_threshold = self.creation_date + timedelta(minutes=PASSWORD_RECOVERY_VALID_TIME)
        if timezone.now() > time_threshold:
            return False
        else:
            return True
    is_valid.fget.short_description = u"Is valid?"
    is_valid.fget.boolean = True


class ValidateEmailCode(BaseCode):

    class Meta:
        verbose_name = 'Validate E-mail Code'
        verbose_name_plural = 'Validate E-mail Codes'

    @property
    def is_valid(self):
        time_threshold = self.creation_date + timedelta(minutes=EMAIL_VALIDATION_VALID_TIME)
        if timezone.now() > time_threshold:
            return False
        else:
            return True
    is_valid.fget.short_description = u"Is valid?"
    is_valid.fget.boolean = True
