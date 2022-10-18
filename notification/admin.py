from django.contrib import admin
from .models import SentNotification, PasswordRecoveryCode, ValidateEmailCode


class SentNotificationAdmin(admin.ModelAdmin):
    list_display = ['id', 'recipient', 'reason']
    search_fields = ['id', 'reason']
    list_filter = ('reason',)


class BaseCodeAdmin(admin.ModelAdmin):
    list_display = ['code', 'user', 'creation_date', 'reason', 'get_is_valid']
    search_fields = ['id', 'user', 'reason']
    list_filter = ['reason', ]
    fields = ['code', 'user', 'creation_date', 'reason', 'get_is_valid']
    readonly_fields = ('get_is_valid', )

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
