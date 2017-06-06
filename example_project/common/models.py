from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.db import models


class Buy(models.Model):
    name = models.CharField('name', max_length=128)

    class Meta:
        verbose_name = 'buy'
        verbose_name_plural = 'buy'

    def __str__(self):
        return self.name


class Sell(models.Model):
    name = models.CharField('name', max_length=128)

    class Meta:
        verbose_name = 'sell'
        verbose_name_plural = 'sells'

    def __str__(self):
        return self.name


class Rent(models.Model):
    name = models.CharField('name', max_length=128)

    class Meta:
        verbose_name = 'rent'
        verbose_name_plural = 'rents'

    def __str__(self):
        return self.name


class Advert(models.Model):
    title = models.CharField('title', max_length=128)
    content = models.TextField('content')
    content_type = models.ForeignKey(ContentType, verbose_name='content type', limit_choices_to={
        'model__in': ['buy', 'sell', 'rent']
    }, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField(db_index=True)
    content_object = GenericForeignKey('content_type', 'object_id')

    def __str__(self):
        return self.title
