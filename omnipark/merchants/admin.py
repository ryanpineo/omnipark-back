from django.contrib import admin

from .models import Merchant


class MerchantAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'visa_merchant_id',)


admin.site.register(Merchant, MerchantAdmin)
