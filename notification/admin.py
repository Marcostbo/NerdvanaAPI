from django.contrib import admin
from .models import SentNotification, PasswordRecoveryCode, ValidateEmailCode


class SentNotificationAdmin(admin.ModelAdmin):
    list_display = ['id', 'recipient', 'reason']
    search_fields = ['id', 'reason']
    list_filter = ('reason',)


class PasswordRecoveryCodeAdmin(admin.ModelAdmin):
    list_display = ['code', 'user', 'creation_date', 'reason']
    search_fields = ['id', 'user', 'reason']
    list_filter = ['reason', ]


class ValidateEmailCodeAdmin(admin.ModelAdmin):
    list_display = ['code', 'user', 'creation_date', 'reason']
    search_fields = ['id', 'user', 'reason']
    list_filter = ['reason', ]


admin.site.register(SentNotification, SentNotificationAdmin)
admin.site.register(PasswordRecoveryCode, PasswordRecoveryCodeAdmin)
admin.site.register(ValidateEmailCode, ValidateEmailCodeAdmin)

