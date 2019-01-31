from django.contrib import admin

from apps.location.models import Location


class LocationAdmin(admin.ModelAdmin):
    list_display = ["timestamp", "latitude", "longitude"]


admin.site.register(Location, LocationAdmin)
