from django.contrib import admin

from clients.models import Client


@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ('full_name','email', 'gender', 'age')
    list_filter = ('gender',)
    search_fields = ('full_name',)