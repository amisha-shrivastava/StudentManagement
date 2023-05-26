from django.contrib import admin
# from django.contrib.auth.admin import UserAdmin
from .models import User


class MyModelAdmin(admin.ModelAdmin):
    list_display = ['name', 'is_active']
    list_editable = ['is_active']

admin.site.register(User, MyModelAdmin)
