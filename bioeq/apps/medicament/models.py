# coding=utf-8

from django.db import models


class Product(models.Model):

    bioequivalent = models.BooleanField()
    name = models.CharField(max_length=50)
    holder = models.ForeignKey('Holder')
    medicinal_ingredient = models.ForeignKey('MedicinalIngredient', verbose_name='Ingrediente Actívo')

    def __unicode__(self):
        return u"%s" % self.name


class Holder(models.Model):

    name = models.CharField(max_length=50)

    def __unicode__(self):
        return u"%s" % self.name


class MedicinalIngredient(models.Model):

    name = models.CharField(max_length=50)
    treatment = models.ForeignKey('Treatment')

    def __unicode__(self):
        return u"%s" % self.name


class Treatment(models.Model):

    name = models.CharField(max_length=50)

    def __unicode__(self):
        return u"%s" % self.name
