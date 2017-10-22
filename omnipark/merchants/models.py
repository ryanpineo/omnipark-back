import requests

from django.db import models
from django.conf import settings


class Merchant(models.Model):
    name = models.CharField(max_length=255)

    # Visa Stuffs
    community_code = models.CharField(max_length=255)
    visa_merchant_id = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.pk:
            created = True
        else:
            created = False
        super().save(*args, **kwargs)
        if created:
            r = requests.post(
                'https://sandbox.api.visa.com/vop/v1/merchants/onboard',
                cert=(settings.VISA_CERT, settings.VISA_PRIVKEY),
                auth=(settings.VISA_USERNAME, settings.VISA_PASSWORD),
                headers={'accept': 'application/json'},
                json={
                    'communityCode': self.community_code,
                    'merchantDetails': [{
                        'visaMerchantId': self.visa_merchant_id,
                    }]
                }
            )


class Offer(models.Model):
    merchant = models.ForeignKey('Merchant', related_name='offers', on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    description = models.TextField()
    start = models.DateTimeField()
    end = models.DateTimeField()
    community_code = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class OfferEvent(models.Model):
    offer = models.ForeignKey('Offer', related_name='events', on_delete=models.CASCADE)


class OfferEventField(models.Model):
    event = models.ForeignKey('OfferEvent', related_name='fields', on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    value = models.CharField(max_length=255)
