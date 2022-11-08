from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import User, Console, Company, Family, Games, GameCompany, Store


class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = User
    list_display = ('email', 'name', 'is_staff', 'is_active',)
    list_filter = ('is_staff', 'is_active',)
    fieldsets = (
        (None, {'fields': ('email', 'name', 'password')}),
        ('Permissions', {'fields': ('is_staff', 'is_active')}),
        ('Email Validation', {'fields': ('email_validated', )})
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2', 'is_staff', 'is_active')}
         ),
    )
    readonly_fields = ('email_validated', )
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
        (None, {'fields': ('name', 'release', 'summary', 'storyline', 'console', 'game_company')}),
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


admin.site.register(User, CustomUserAdmin)
admin.site.register(Console, ConsoleAdmin)
admin.site.register(Company, CompanyAdmin)
admin.site.register(Games, GameAdmin)
admin.site.register(Family, FamilyAdmin)
admin.site.register(GameCompany, GameCompanyAdmin)
admin.site.register(Store, StoreAdmin)
