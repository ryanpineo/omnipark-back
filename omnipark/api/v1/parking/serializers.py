from rest_framework import serializers

from omnipark.parking.models import Spot, Booking, BookingStatus


class SpotSerializer(serializers.ModelSerializer):
    class Meta:
        model = Spot
        fields = ('id', 'type', 'address_line1', 'address_line2',
                  'address_city', 'address_state', 'address_postalcode',
                  'location',)

    def to_representation(self, obj):
        r = super().to_representation(obj)
        r['location'] = {}
        r['location']['lat'] = obj.location.y
        r['location']['long'] = obj.location.x
        return r


class BookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = ('id', 'spot', 'start', 'end',)

    def create(self, validated_data):
        validated_data['user'] = self.context['request'].user
        validated_data['status'] = BookingStatus.ACTIVE
        return super().create(validated_data)


class BookingExtendSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = ('id', 'end',)
