from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import User, Console, Company, Family


class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = User
    list_display = ('email', 'name', 'is_staff', 'is_active',)
    list_filter = ('is_staff', 'is_active',)
    fieldsets = (
        (None, {'fields': ('email', 'name', 'password')}),
        ('Permissions', {'fields': ('is_staff', 'is_active')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2', 'is_staff', 'is_active')}
         ),
    )
    search_fields = ('email',)
    ordering = ('email',)


class ConsoleAdmin(admin.ModelAdmin):
    list_display = ['name', 'initials', 'release', 'family', 'company']
    search_fields = ['id', 'name', 'initials']


class FamilyAdmin(admin.ModelAdmin):
    list_display = ['name']
    search_fields = ['id', 'name']


class CompanyAdmin(admin.ModelAdmin):
    list_display = ['name']
    search_fields = ['id', 'name']


admin.site.register(User, CustomUserAdmin)
admin.site.register(Console, ConsoleAdmin)
admin.site.register(Company, CompanyAdmin)
admin.site.register(Family, FamilyAdmin)

