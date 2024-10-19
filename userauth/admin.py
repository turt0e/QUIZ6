# admin.py
from django.contrib import admin
from .models import User

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('email', 'username', 'is_active', 'is_admin')
    list_filter = ('is_active', 'is_admin')
    search_fields = ('email', 'username')
    ordering = ('email',)

# Register your models here.
