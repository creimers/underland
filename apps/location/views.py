from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from apps.location.models import Location


class LocationView(APIView):
    def post(self, request, format=None):
        """
        create location instances
        """

        locations = request.data.get("locations", None)
        if locations:
            for location in locations:
                Location.objects.create(data=location)
        return Response({"result": "ok"}, status=status.HTTP_201_CREATED)
