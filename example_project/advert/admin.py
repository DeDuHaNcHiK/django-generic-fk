from django.contrib import admin

from advert.models import Advert, Rent, Sell, Buy
from generic_fk.mixins import ModelAdminMixin


class AdvertAdmin(ModelAdminMixin, admin.ModelAdmin):
    pass


admin.site.register(Advert, AdvertAdmin)
admin.site.register(Buy)
admin.site.register(Sell)
admin.site.register(Rent)
