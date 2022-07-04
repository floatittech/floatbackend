from django.contrib import admin
from .models import *


class UserDetailAdmin(admin.ModelAdmin):
    readonly_fields = ["created_at", "updated_at"]
    fields = [field.name for field in UserDetail._meta.fields if field.name != "id"]
admin.site.register(UserDetail, UserDetailAdmin)


class ScreenshotAdmin(admin.ModelAdmin):
    readonly_fields = ["created_at", "updated_at"]
    fields = [field.name for field in Screenshot._meta.fields if field.name != "id"]
admin.site.register(Screenshot, ScreenshotAdmin)
