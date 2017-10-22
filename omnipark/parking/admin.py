from django.contrib import admin
from django.contrib.gis import forms
from django.contrib.gis.admin import GeoModelAdmin

from fsm_admin.mixins import FSMTransitionMixin

from .models import Spot, Booking


class SpotAdminForm(forms.ModelForm):
    location = forms.PointField(widget=forms.OSMWidget(attrs={'display_raw': True}))


class SpotAdmin(GeoModelAdmin):
    list_display = ('id', 'user', 'type', 'address_line1', 'address_city',)
    form = SpotAdminForm


class BookingAdmin(FSMTransitionMixin, admin.ModelAdmin):
    list_display = ('id', 'spot', 'start', 'end', 'status',)
    fsm_field = ['valid_status']


admin.site.register(Spot, SpotAdmin)
admin.site.register(Booking, BookingAdmin)
