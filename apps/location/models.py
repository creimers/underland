from django.contrib.postgres.fields import JSONField
from django.db import models


class Location(models.Model):
    data = JSONField()

    @property
    def timestamp(self):
        return self.data["properties"]["timestamp"]

    @property
    def latitude(self):
        return self.data["geometry"]["coordinates"][1]

    @property
    def longitude(self):
        return self.data["geometry"]["coordinates"][0]
