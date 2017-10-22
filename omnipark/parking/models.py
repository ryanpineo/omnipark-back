import enum

from django.db import models
from django.conf import settings
from django.contrib.gis.db.models import PointField

from django_fsm import FSMIntegerField, transition
from push_notifications.models import APNSDevice


class SpotType(enum.Enum):
    PRIVATE = 'private'
    COMMERCIAL = 'commercial'
    PUBLIC = 'public'


class Spot(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='spots', on_delete=models.CASCADE)
    type = models.CharField(
        max_length=255,
        choices=(
            (SpotType.PRIVATE.value, 'Private'),
            (SpotType.COMMERCIAL.value, 'Commercial'),
            (SpotType.PUBLIC.value, 'Public'),
        )
    )
    address_line1 = models.CharField(max_length=255)
    address_line2 = models.CharField(max_length=255, blank=True)
    address_city = models.CharField(max_length=255)
    address_state = models.CharField(max_length=255)
    address_postalcode = models.CharField(max_length=255)
    location = PointField()


class BookingStatus(enum.IntEnum):
    ACTIVE = 1
    EXPIRED = 2


class Booking(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='bookings', on_delete=models.CASCADE)
    spot = models.ForeignKey('Spot', related_name='bookings', on_delete=models.CASCADE)

    start = models.DateTimeField()
    end = models.DateTimeField()
    status = FSMIntegerField(
        choices=(
            (BookingStatus.ACTIVE.value, 'Active'),
            (BookingStatus.EXPIRED.value, 'Expired'),
        )
    )

    def save(self, *args, **kwargs):
        if not self.pk:
            created = True
        else:
            created = False
        super().save(*args, **kwargs)
        if created:
            devices = APNSDevice.objects.filter(user=self.spot.user)
            devices.send_message('Your parking spot has been booked!')

    @transition(status, source=BookingStatus.ACTIVE.value, target=BookingStatus.EXPIRED.value)
    def expire(self):
        pass
        # pull funds
        # push funds
        # notification to driver
        # notification to spot owner
