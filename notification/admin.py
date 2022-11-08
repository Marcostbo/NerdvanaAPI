from django.contrib import admin
from .models import SentNotification, PasswordRecoveryCode, ValidateEmailCode


class SentNotificationAdmin(admin.ModelAdmin):
    list_display = ['id', 'recipient', 'reason', 'sent']
    search_fields = ['id', 'reason']
    list_filter = ('reason', 'sent')


class BaseCodeAdmin(admin.ModelAdmin):
    list_display = ['code', 'user', 'creation_date', 'reason', 'get_is_valid', 'validated']
    search_fields = ['id', 'user', 'reason']
    list_filter = ['creation_date', 'validated', ]
    fields = ['code', 'user', 'creation_date', 'reason', 'get_is_valid', 'validated']
    readonly_fields = ('get_is_valid', 'validated', 'creation_date')

    @staticmethod
    @admin.display(boolean=True, description='Is valid?')
    def get_is_valid(instance):
        return instance.is_valid


class PasswordRecoveryCodeAdmin(BaseCodeAdmin):
    pass


class ValidateEmailCodeAdmin(BaseCodeAdmin):
    pass


admin.site.register(SentNotification, SentNotificationAdmin)
admin.site.register(PasswordRecoveryCode, PasswordRecoveryCodeAdmin)
admin.site.register(ValidateEmailCode, ValidateEmailCodeAdmin)
