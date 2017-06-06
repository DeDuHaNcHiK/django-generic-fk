Description
===========

'django-generic-fk' is essentially just a collection of widgets and mixin for easy use GenericForeignKey in Django admin.

Usage
=====

Mixin
-----

In file ``admin.py``::

         from django.contrib import admin

         from apps.models import SomeModel
         from generic_fk.mixins import ModelAdminMixin


         class SomeModelAdmin(ModelAdminMixin, admin.ModelAdmin):
             pass

         admin.site.register(SomeModel, SomeModelAdmin)

Widget
------

In file ``admin.py``::

         from django.contrib import admin
         from django.contrib.admin.widgets import ForeignKeyRawIdWidget
         from django.core.exceptions import ObjectDoesNotExist
         from django.db.models import ManyToOneRel
         from django import forms

         from apps.models import SomeModel
         from generic_fk.widgets import ContentTypeSelect


         class SomeModelForm(forms.ModelForm):
             def __init__(self, *args, **kwargs):
                 super(SomeModelForm, self).__init__(*args, **kwargs)
                 try:
                     model = self.instance.content_type.model_class()
                     model_key = model._meta.pk.name
                 except (AttributeError, ObjectDoesNotExist):
                     model = self.fields['content_type'].queryset[0].model_class()
                     model_key = 'id'
                 self.fields['object_id'].widget = ForeignKeyRawIdWidget(
                     rel=ManyToOneRel(model, model_key),
                     admin_site=admin.site
                 )

             class Meta:
                 model = SomeModel
                 widgets = {
                     'content_type': ContentTypeSelect
                 }

         class SomeModelAdmin(admin.ModelAdmin):
             form = SomeModelForm

         admin.site.register(SomeModel, SomeModelAdmin)
