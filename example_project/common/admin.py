from django import forms
from django.contrib import admin
from django.contrib.admin.widgets import ForeignKeyRawIdWidget
from django.core.exceptions import ObjectDoesNotExist
from django.db.models import ManyToOneRel

from common.models import Buy, Rent, Sell, Advert
# from generic_fk.mixins import ModelAdminMixin
from generic_fk.widgets import ContentTypeSelect


class AdvertModelForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(AdvertModelForm, self).__init__(*args, **kwargs)
        try:
            model = self.instance.content_type.model_class()
            model_key = model._meta.pk.name
        except (AttributeError, ObjectDoesNotExist):
            model = self.fields['content_type'].queryset[0].model_class()
            model_key = 'id'
        self.fields['object_id'].widget = ForeignKeyRawIdWidget(
            rel=ManyToOneRel(model_key, model, 'id'),
            admin_site=admin.site
        )

    class Meta:
        model = Advert
        fields = "__all__"
        widgets = {
            'content_type': ContentTypeSelect
        }


class AdvertAdmin(admin.ModelAdmin):
    form = AdvertModelForm


# class AdvertAdmin(ModelAdminMixin, admin.ModelAdmin):
#     pass


admin.site.register(Buy)
admin.site.register(Sell)
admin.site.register(Rent)
admin.site.register(Advert, AdvertAdmin)
