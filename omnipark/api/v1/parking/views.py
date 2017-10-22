from rest_framework import viewsets, mixins, permissions, response
from rest_framework.decorators import detail_route

from omnipark.parking.models import Spot

from .serializers import SpotSerializer, BookingSerializer, BookingExtendSerializer


class SpotsViewSet(mixins.ListModelMixin,
                   viewsets.GenericViewSet):
    serializer_class = SpotSerializer
    queryset = Spot.objects.all()


class BookingsViewSet(mixins.CreateModelMixin,
                      viewsets.GenericViewSet):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = BookingSerializer

    @detail_route(methods=['POST'], serializer_class=BookingExtendSerializer)
    def extend(self, request, pk=None):
        booking = self.get_object()
        serializer = self.get_serializer(instance=booking, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return response.Response(serializer.data)
