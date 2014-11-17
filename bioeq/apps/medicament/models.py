# coding=utf-8

from django.db import models


class Product(models.Model):

    bioequivalent = models.BooleanField(verbose_name="Bioequivalente")
    name = models.CharField(max_length=96, verbose_name='Detalle')
    holder = models.ForeignKey('Holder', verbose_name='Titular')
    registry = models.CharField(max_length=10, blank=True, verbose_name="'Registro")
    medicinal_ingredient = models.ForeignKey('MedicinalIngredient', verbose_name='Ingrediente Actívo')

    def __unicode__(self):
        return u"%s" % self.name


class Holder(models.Model):

    name = models.CharField(max_length=50)

    def __unicode__(self):
        return u"%s" % self.name


class MedicinalIngredient(models.Model):

    name = models.CharField(max_length=50)
    treatment = models.ForeignKey('Treatment', default=None, null=True, blank=True)

    def __unicode__(self):
        return u"%s" % self.name


class Treatment(models.Model):

    name = models.CharField(max_length=120)

    def __unicode__(self):
        return u"%s" % self.name
