# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Departamento'
        db.create_table(u'inventario_departamento', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('municipio', self.gf('django.db.models.fields.CharField')(max_length=50)),
        ))
        db.send_create_signal(u'inventario', ['Departamento'])

        # Adding model 'Usuario'
        db.create_table(u'inventario_usuario', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('identificacion', self.gf('django.db.models.fields.CharField')(unique=True, max_length=20)),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('apellido', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('direccion', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('telefono', self.gf('django.db.models.fields.CharField')(max_length=20)),
            ('sexo', self.gf('django.db.models.fields.CharField')(default='Masculino', max_length=15)),
            ('estado', self.gf('django.db.models.fields.BooleanField')(default=True)),
        ))
        db.send_create_signal(u'inventario', ['Usuario'])

        # Adding model 'Rol'
        db.create_table(u'inventario_rol', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('usuario', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['inventario.Usuario'])),
        ))
        db.send_create_signal(u'inventario', ['Rol'])

        # Adding model 'Proveedor'
        db.create_table(u'inventario_proveedor', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('identificacion', self.gf('django.db.models.fields.CharField')(unique=True, max_length=50)),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('apellido', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('telefono', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('direccion', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('email', self.gf('django.db.models.fields.EmailField')(max_length=75)),
            ('razon_social', self.gf('django.db.models.fields.CharField')(max_length=50)),
        ))
        db.send_create_signal(u'inventario', ['Proveedor'])

        # Adding model 'CodigoBarras'
        db.create_table(u'inventario_codigobarras', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('codigo', self.gf('django.db.models.fields.CharField')(unique=True, max_length=13)),
            ('fecha', self.gf('django.db.models.fields.DateField')(auto_now=True, blank=True)),
        ))
        db.send_create_signal(u'inventario', ['CodigoBarras'])

        # Adding model 'Producto'
        db.create_table(u'inventario_producto', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('referencia', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('fecha_ingreso', self.gf('django.db.models.fields.DateField')()),
            ('ancho', self.gf('django.db.models.fields.CharField')(max_length=10)),
            ('largo', self.gf('django.db.models.fields.CharField')(max_length=10)),
            ('proveedor', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['inventario.Proveedor'])),
            ('codigobarras', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['inventario.CodigoBarras'])),
            ('valor', self.gf('django.db.models.fields.IntegerField')()),
            ('descripcion', self.gf('django.db.models.fields.TextField')(max_length=150)),
            ('cantidad', self.gf('django.db.models.fields.IntegerField')(default=0)),
        ))
        db.send_create_signal(u'inventario', ['Producto'])

        # Adding model 'Sede'
        db.create_table(u'inventario_sede', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nombre_sede', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('direccion', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('telefono', self.gf('django.db.models.fields.CharField')(max_length=20)),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('referencia', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('fecha_ingreso', self.gf('django.db.models.fields.DateField')(auto_now=True, blank=True)),
            ('dimensiones', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('proveedor', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['inventario.Proveedor'])),
            ('codigobarras', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['inventario.CodigoBarras'])),
            ('valor', self.gf('django.db.models.fields.IntegerField')()),
            ('descripcion', self.gf('django.db.models.fields.TextField')(max_length=150)),
            ('cantidad', self.gf('django.db.models.fields.IntegerField')(default=0)),
        ))
        db.send_create_signal(u'inventario', ['Sede'])

        # Adding model 'Salida'
        db.create_table(u'inventario_salida', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('codigobarras', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['inventario.CodigoBarras'])),
            ('fecha_salida', self.gf('django.db.models.fields.DateField')(auto_now=True, blank=True)),
            ('tipo_salida', self.gf('django.db.models.fields.CharField')(default='traslado', max_length=50)),
            ('producto', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['inventario.Producto'])),
            ('cantidad', self.gf('django.db.models.fields.IntegerField')()),
            ('sede', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['inventario.Sede'])),
            ('descripcion', self.gf('django.db.models.fields.TextField')(max_length=150)),
            ('numero_contrato', self.gf('django.db.models.fields.IntegerField')()),
        ))
        db.send_create_signal(u'inventario', ['Salida'])

        # Adding model 'Entrada'
        db.create_table(u'inventario_entrada', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('fecha_ingreso', self.gf('django.db.models.fields.DateField')(auto_now=True, blank=True)),
            ('producto', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['inventario.Producto'])),
            ('cantidad', self.gf('django.db.models.fields.IntegerField')()),
            ('observacion', self.gf('django.db.models.fields.TextField')(max_length=500)),
        ))
        db.send_create_signal(u'inventario', ['Entrada'])


    def backwards(self, orm):
        # Deleting model 'Departamento'
        db.delete_table(u'inventario_departamento')

        # Deleting model 'Usuario'
        db.delete_table(u'inventario_usuario')

        # Deleting model 'Rol'
        db.delete_table(u'inventario_rol')

        # Deleting model 'Proveedor'
        db.delete_table(u'inventario_proveedor')

        # Deleting model 'CodigoBarras'
        db.delete_table(u'inventario_codigobarras')

        # Deleting model 'Producto'
        db.delete_table(u'inventario_producto')

        # Deleting model 'Sede'
        db.delete_table(u'inventario_sede')

        # Deleting model 'Salida'
        db.delete_table(u'inventario_salida')

        # Deleting model 'Entrada'
        db.delete_table(u'inventario_entrada')


    models = {
        u'inventario.codigobarras': {
            'Meta': {'object_name': 'CodigoBarras'},
            'codigo': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '13'}),
            'fecha': ('django.db.models.fields.DateField', [], {'auto_now': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'inventario.departamento': {
            'Meta': {'object_name': 'Departamento'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'municipio': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'inventario.entrada': {
            'Meta': {'object_name': 'Entrada'},
            'cantidad': ('django.db.models.fields.IntegerField', [], {}),
            'fecha_ingreso': ('django.db.models.fields.DateField', [], {'auto_now': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'observacion': ('django.db.models.fields.TextField', [], {'max_length': '500'}),
            'producto': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['inventario.Producto']"})
        },
        u'inventario.producto': {
            'Meta': {'object_name': 'Producto'},
            'ancho': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            'cantidad': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'codigobarras': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['inventario.CodigoBarras']"}),
            'descripcion': ('django.db.models.fields.TextField', [], {'max_length': '150'}),
            'fecha_ingreso': ('django.db.models.fields.DateField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'largo': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'proveedor': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['inventario.Proveedor']"}),
            'referencia': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'valor': ('django.db.models.fields.IntegerField', [], {})
        },
        u'inventario.proveedor': {
            'Meta': {'object_name': 'Proveedor'},
            'apellido': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'direccion': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'identificacion': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '50'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'razon_social': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'telefono': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'inventario.rol': {
            'Meta': {'object_name': 'Rol'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'usuario': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['inventario.Usuario']"})
        },
        u'inventario.salida': {
            'Meta': {'object_name': 'Salida'},
            'cantidad': ('django.db.models.fields.IntegerField', [], {}),
            'codigobarras': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['inventario.CodigoBarras']"}),
            'descripcion': ('django.db.models.fields.TextField', [], {'max_length': '150'}),
            'fecha_salida': ('django.db.models.fields.DateField', [], {'auto_now': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'numero_contrato': ('django.db.models.fields.IntegerField', [], {}),
            'producto': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['inventario.Producto']"}),
            'sede': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['inventario.Sede']"}),
            'tipo_salida': ('django.db.models.fields.CharField', [], {'default': "'traslado'", 'max_length': '50'})
        },
        u'inventario.sede': {
            'Meta': {'object_name': 'Sede'},
            'cantidad': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'codigobarras': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['inventario.CodigoBarras']"}),
            'descripcion': ('django.db.models.fields.TextField', [], {'max_length': '150'}),
            'dimensiones': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'direccion': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'fecha_ingreso': ('django.db.models.fields.DateField', [], {'auto_now': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'nombre_sede': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'proveedor': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['inventario.Proveedor']"}),
            'referencia': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'telefono': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'valor': ('django.db.models.fields.IntegerField', [], {})
        },
        u'inventario.usuario': {
            'Meta': {'object_name': 'Usuario'},
            'apellido': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'direccion': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'estado': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'identificacion': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '20'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'sexo': ('django.db.models.fields.CharField', [], {'default': "'Masculino'", 'max_length': '15'}),
            'telefono': ('django.db.models.fields.CharField', [], {'max_length': '20'})
        }
    }

    complete_apps = ['inventario']