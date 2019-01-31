from django.contrib import admin
from import_export import resources
from import_export.admin import ImportExportModelAdmin
from import_export.fields import Field

from apps.location.models import Location


class LocationResource(resources.ModelResource):
    class Meta:
        model = Location
        exclude = ("id", "data")

    timestamp = Field()
    latitude = Field()
    longitude = Field()

    def dehydrate_timestamp(self, location):
        return location.timestamp

    def dehydrate_latitude(self, location):
        return location.latitude

    def dehydrate_longitude(self, location):
        return location.longitude


class LocationAdmin(ImportExportModelAdmin):
    list_display = ["timestamp", "latitude", "longitude"]
    resource_class = LocationResource


admin.site.register(Location, LocationAdmin)
