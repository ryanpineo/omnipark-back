from rest_framework import viewsets, mixins, permissions

from omnipark.parking.models import Spot

from .serializers import SpotSerializer, BookingSerializer


class SpotsViewSet(mixins.ListModelMixin,
                   viewsets.GenericViewSet):
    serializer_class = SpotSerializer
    queryset = Spot.objects.all()


class BookingsViewSet(mixins.CreateModelMixin,
                      viewsets.GenericViewSet):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = BookingSerializer
