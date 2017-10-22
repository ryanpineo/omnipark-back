from django.contrib import admin

import nested_admin

from .models import Merchant, Offer, OfferEvent, OfferEventField


class MerchantAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'visa_merchant_id',)


class OfferEventFieldInline(nested_admin.NestedStackedInline):
    model = OfferEventField


class OfferEventInline(nested_admin.NestedStackedInline):
    model = OfferEvent
    inlines = [OfferEventFieldInline]


class OfferAdmin(nested_admin.NestedModelAdmin):
    inlines = [OfferEventInline]


admin.site.register(Merchant, MerchantAdmin)
admin.site.register(Offer, OfferAdmin)
