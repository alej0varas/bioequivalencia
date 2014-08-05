# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):

        # Changing field 'MedicinalIngredient.treatment'
        db.alter_column(u'medicament_medicinalingredient', 'treatment_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['medicament.Treatment'], null=True))
        # Adding field 'Product.registry'
        db.add_column(u'medicament_product', 'registry',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=10, blank=True),
                      keep_default=False)


    def backwards(self, orm):

        # Changing field 'MedicinalIngredient.treatment'
        db.alter_column(u'medicament_medicinalingredient', 'treatment_id', self.gf('django.db.models.fields.related.ForeignKey')(default=None, to=orm['medicament.Treatment']))
        # Deleting field 'Product.registry'
        db.delete_column(u'medicament_product', 'registry')


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
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'registry': ('django.db.models.fields.CharField', [], {'max_length': '10', 'blank': 'True'})
        },
        u'medicament.treatment': {
            'Meta': {'object_name': 'Treatment'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        }
    }

    complete_apps = ['medicament']