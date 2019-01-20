import pytest
from django.urls import reverse

from apps.location.models import Location

PAYLOAD = {
    "locations": [
        {
            "type": "Feature",
            "geometry": {
                "type": "Point",
                "coordinates": {"latitude": 37.331800, "longitude": -122.030581},
            },
            "properties": {
                "timestamp": "2015-10-01T08:00:00-0700",
                "altitude": 0,
                "speed": 4,
                "horizontal_accuracy": 30,
                "vertical_accuracy": -1,
                "motion": ["driving", "stationary"],
                "pauses": "false",
                "activity": "other_navigation",
                "desired_accuracy": 100,
                "deferred": 1000,
                "significant_change": "disabled",
                "locations_in_payload": 1,
                "device_id": "",
                "wifi": "launchpad",
                "battery_state": "charging",
                "battery_level": 0.89,
            },
        },
        {
            "type": "Feature",
            "geometry": {
                "type": "Point",
                "coordinates": {"latitude": 37.331800, "longitude": -122.030581},
            },
            "properties": {
                "timestamp": "2015-10-01T08:00:00-0700",
                "altitude": 0,
                "speed": 4,
                "horizontal_accuracy": 30,
                "vertical_accuracy": -1,
                "motion": ["driving", "stationary"],
                "pauses": "false",
                "activity": "other_navigation",
                "desired_accuracy": 100,
                "deferred": 1000,
                "significant_change": "disabled",
                "locations_in_payload": 1,
                "device_id": "",
                "wifi": "launchpad",
                "battery_state": "charging",
                "battery_level": 0.89,
            },
        },
    ]
}


@pytest.mark.django_db
def test_POST_201(rest_client):
    url = reverse("location-collection")
    response = rest_client.post(url, PAYLOAD, format="json")

    assert response.status_code == 201
    assert Location.objects.all().count() == len(PAYLOAD["locations"])
