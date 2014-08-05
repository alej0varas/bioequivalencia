# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Product'
        db.create_table(u'medicament_product', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('bioequivalent', self.gf('django.db.models.fields.BooleanField')()),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('holder', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['medicament.Holder'])),
            ('medicinal_ingredient', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['medicament.MedicinalIngredient'])),
        ))
        db.send_create_signal(u'medicament', ['Product'])

        # Adding model 'Holder'
        db.create_table(u'medicament_holder', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=50)),
        ))
        db.send_create_signal(u'medicament', ['Holder'])

        # Adding model 'MedicinalIngredient'
        db.create_table(u'medicament_medicinalingredient', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('treatment', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['medicament.Treatment'])),
        ))
        db.send_create_signal(u'medicament', ['MedicinalIngredient'])

        # Adding model 'Treatment'
        db.create_table(u'medicament_treatment', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=50)),
        ))
        db.send_create_signal(u'medicament', ['Treatment'])


    def backwards(self, orm):
        # Deleting model 'Product'
        db.delete_table(u'medicament_product')

        # Deleting model 'Holder'
        db.delete_table(u'medicament_holder')

        # Deleting model 'MedicinalIngredient'
        db.delete_table(u'medicament_medicinalingredient')

        # Deleting model 'Treatment'
        db.delete_table(u'medicament_treatment')


    models = {
        u'medicament.holder': {
            'Meta': {'object_name': 'Holder'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'medicament.medicinalingredient': {
            'Meta': {'object_name': 'MedicinalIngredient'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'treatment': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['medicament.Treatment']"})
        },
        u'medicament.product': {
            'Meta': {'object_name': 'Product'},
            'bioequivalent': ('django.db.models.fields.BooleanField', [], {}),
            'holder': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['medicament.Holder']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'medicinal_ingredient': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['medicament.MedicinalIngredient']"}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'medicament.treatment': {
            'Meta': {'object_name': 'Treatment'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        }
    }

    complete_apps = ['medicament']