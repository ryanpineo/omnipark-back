from rest_framework import viewsets, mixins, permissions

from omnipark.merchants.models import Offer

from .serializers import OfferSerializer


class OffersViewSet(mixins.ListModelMixin,
                    viewsets.GenericViewSet):
    serializer_class = OfferSerializer
    queryset = Offer.objects.all()
