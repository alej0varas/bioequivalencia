# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Changing field 'Treatment.name'
        db.alter_column(u'medicament_treatment', 'name', self.gf('django.db.models.fields.CharField')(max_length=96))

    def backwards(self, orm):
        # Changing field 'Treatment.name'
        db.alter_column(u'medicament_treatment', 'name', self.gf('django.db.models.fields.CharField')(max_length=50))

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
            'treatment': ('django.db.models.fields.related.ForeignKey', [], {'default': 'None', 'to': u"orm['medicament.Treatment']", 'null': 'True', 'blank': 'True'})
        },
        u'medicament.product': {
            'Meta': {'object_name': 'Product'},
            'bioequivalent': ('django.db.models.fields.BooleanField', [], {}),
            'holder': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['medicament.Holder']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'medicinal_ingredient': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['medicament.MedicinalIngredient']"}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '96'}),
            'registry': ('django.db.models.fields.CharField', [], {'max_length': '10', 'blank': 'True'})
        },
        u'medicament.treatment': {
            'Meta': {'object_name': 'Treatment'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '96'})
        }
    }

    complete_apps = ['medicament']