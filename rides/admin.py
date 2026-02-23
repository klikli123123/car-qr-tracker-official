from django.contrib import admin
from .models import Ride, Fine


@admin.register(Ride)
class RideAdmin(admin.ModelAdmin):
    list_display = ("driver", "started_at", "ended_at")
    list_filter = ("driver",)


@admin.register(Fine)
class FineAdmin(admin.ModelAdmin):
    list_display = ("happened_at", "driver_at_time", "ride", "notes")
    readonly_fields = ("driver_at_time", "ride", "created_at")

    def save_model(self, request, obj, form, change):
        obj.resolve_driver()
        super().save_model(request, obj, form, change)


