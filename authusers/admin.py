from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as CustomUserAdmin
from .models import User

class UserAdmin(CustomUserAdmin):
    list_display = ('email','is_staff','is_superuser','username') 

admin.site.register(User, UserAdmin)

