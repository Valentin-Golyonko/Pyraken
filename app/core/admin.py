from django.contrib import admin

from app.core.models import Flag


@admin.register(Flag)
class FlagAdmin(admin.ModelAdmin):
    pass
