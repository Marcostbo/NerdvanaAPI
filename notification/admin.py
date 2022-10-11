from django.contrib import admin
from .models import SentNotification


class SentNotificationAdmin(admin.ModelAdmin):
    list_display = ['id', 'recipient', 'reason']
    search_fields = ['id', 'reason']
    list_filter = ('reason',)


admin.register(SentNotification, SentNotificationAdmin)

