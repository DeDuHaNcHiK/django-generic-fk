# coding: utf-8
from functools import partial
from django.contrib import admin
from django.contrib.admin import ModelAdmin
from django.contrib.admin.util import flatten_fieldsets
from django.contrib.admin.widgets import ForeignKeyRawIdWidget
from django.core.exceptions import ObjectDoesNotExist
from django.db.models import ManyToOneRel
from django.forms.models import (modelform_factory,)
from generic_fk.widgets import ContentTypeSelect


class ModelAdminMixin(object):
    def get_form(self, request, obj=None, **kwargs):
        if self.declared_fieldsets:
            fields = flatten_fieldsets(self.declared_fieldsets)
        else:
            fields = None
        if self.exclude is None:
            exclude = []
        else:
            exclude = list(self.exclude)
        exclude.extend(self.get_readonly_fields(request, obj))
        if self.exclude is None and hasattr(self.form, '_meta') and self.form._meta.exclude:
            # Take the custom ModelForm's Meta.exclude into account only if the
            # ModelAdmin doesn't define its own.
            exclude.extend(self.form._meta.exclude)
        # if exclude is an empty list we pass None to be consistant with the
        # default on modelform_factory
        exclude = exclude or None

        try:
            model = obj.content_type.model_class()
            model_key = model._meta.pk.name
        except (AttributeError, ObjectDoesNotExist):
            model = self.model.content_type.field.formfield().choices.queryset[0].model_class()
            model_key = 'id'

        defaults = {
            "form": self.form,
            "fields": fields,
            "exclude": exclude,
            "formfield_callback": partial(self.formfield_for_dbfield, request=request),
            "widgets": {
                'content_type': ContentTypeSelect,
                'object_id': ForeignKeyRawIdWidget(
                    rel=ManyToOneRel(model, model_key),
                    admin_site=admin.site
                )
            }
        }
        defaults.update(kwargs)
        return modelform_factory(self.model, **defaults)
