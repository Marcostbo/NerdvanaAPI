from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import User, Console, Company, Family, Games, GameCompany, Store, PriceAlert


class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = User
    list_display = ('email', 'name', 'is_staff', 'is_active',)
    list_filter = ('is_staff', 'is_active',)
    fieldsets = (
        (None, {'fields': ('email', 'name', 'password', 'password_changed')}),
        ('Permissions', {'fields': ('is_staff', 'is_active')}),
        ('Email Validation', {'fields': ('validated_on', 'email_validated', )})
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2', 'is_staff', 'is_active')}
         ),
    )
    readonly_fields = ('validated_on', 'email_validated', )
    search_fields = ('email',)
    ordering = ('email',)


class StoreAdmin(admin.ModelAdmin):
    list_display = ['name', 'search_name']
    search_fields = ['name']


class GameAdmin(admin.ModelAdmin):
    list_display = ['name', 'release', 'rating']
    search_fields = ['id', 'name']
    list_filter = ('console',)
    filter_horizontal = ('console',)
    fieldsets = (
        (None, {'fields': ('name', 'game_cover_link', 'release', 'summary', 'storyline', 'console', 'game_company')}),
        ('Twitch Ratings', {'fields': ('rating', 'rating_count')})
    )


class GameInline(admin.TabularInline):
    model = Games
    fields = ['name', 'release', 'console']
    extra = 0


class ConsoleAdmin(admin.ModelAdmin):
    list_display = ['name', 'initials', 'release', 'family', 'company', 'twitch_id']
    search_fields = ['id', 'name', 'initials']
    list_filter = ('family',)


class ConsoleInline(admin.TabularInline):
    model = Console
    fields = ['name', 'initials', 'release', 'family', 'company', 'twitch_id']
    extra = 0


class FamilyAdmin(admin.ModelAdmin):
    list_display = ['name']
    search_fields = ['id', 'name']
    inlines = [
        ConsoleInline
    ]


class CompanyAdmin(admin.ModelAdmin):
    list_display = ['name']
    search_fields = ['id', 'name']


class GameCompanyAdmin(admin.ModelAdmin):
    list_display = ['name', 'country']
    search_fields = ['id', 'name']
    list_filter = ['country']
    inlines = [
        GameInline
    ]


class PriceAlertAdmin(admin.ModelAdmin):
    list_display = ['game', 'console', 'user', 'price', 'created_on', 'is_resolved']
    search_fields = ['id', 'game']
    list_filter = ['is_resolved']
    readonly_fields = ('user', 'game', 'console', 'created_on')
    fieldsets = (
        (None, {'fields': ('created_on', 'user', 'game', 'console', 'price', 'is_resolved')}),
        ('Alert Resolving', {'fields': ('price_resolved', 'link_resolved', 'resolved_on')})
    )


admin.site.register(User, CustomUserAdmin)
admin.site.register(Console, ConsoleAdmin)
admin.site.register(Company, CompanyAdmin)
admin.site.register(Games, GameAdmin)
admin.site.register(Family, FamilyAdmin)
admin.site.register(GameCompany, GameCompanyAdmin)
admin.site.register(Store, StoreAdmin)
admin.site.register(PriceAlert, PriceAlertAdmin)
