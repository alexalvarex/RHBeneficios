from __future__ import unicode_literals

from django.db import models

from django.utils.encoding import python_2_unicode_compatible
from django.contrib.auth.models import User
from django.utils import timezone
now = timezone.now()

@python_2_unicode_compatible
class Sexo(models.Model):
	sexo = models.CharField(max_length=9)

	def __str__(self):
		return self.sexo

@python_2_unicode_compatible
class Pais(models.Model):
	pais = models.CharField(max_length=50)

	def __str__(self):
		return self.pais

@python_2_unicode_compatible
class Depto(models.Model):
	depto = models.CharField(max_length=50)
	pais = models.ForeignKey(Pais)

	def __str__(self):
		return self.depto

@python_2_unicode_compatible
class Municipio(models.Model):
	municipio = models.CharField(max_length=50)
	depto = models.ForeignKey(Depto)

	def __str__(self):
		return self.municipio

@python_2_unicode_compatible
class Perfil(models.Model):
	numid = models.CharField(max_length=15)	
	direccion = models.CharField(max_length=100)
	telefono_f = models.CharField(max_length=9, blank=True, null=True)
	telefono_c = models.CharField(max_length=9, blank=True, null=True)
	usuario = models.OneToOneField(User, related_name='Perfil')
	sexo = models.ForeignKey(Sexo, null=True, blank=True)
	es_admin = models.BooleanField(default=False)
	es_secre = models.BooleanField(default=False)
	es_docente = models.BooleanField(default=False)
	es_tutor = models.BooleanField(default=False)

	def __str__(self):
		return self.usuario.username

@python_2_unicode_compatible
class Comunidad(models.Model):
	nombreComunidad = models.CharField(max_length=100)
	municipio = models.ForeignKey(Municipio)

	def __str__(self):
		return self.nombreComunidad


class Lote(models.Model):
	numLote = models.IntegerField()

@python_2_unicode_compatible
class ComunidadLote(models.Model):
	comunidad = models.ForeignKey(Comunidad)
	lote = models.ForeignKey(Lote)

	class Meta:
		unique_together = ('comunidad', 'lote')

	def _comlo(self):
		return "%s %s" %(self.comunidad, self.lote)

	comlo = property(_comlo)

	def __str__(self):
		return self.comlo

class Mapa(models.Model):
	comunidadInicio = models.ForeignKey(Comunidad, related_name='Inicio')
	comunidadFinal = models.ForeignKey(Comunidad, related_name='Final')


@python_2_unicode_compatible
class Criterio(models.Model):
	criterio = models.CharField(max_length= 50)

	def __str__(self):
		return self.criterio


class Capa(models.Model):
	capa = models.CharField(max_length= 50)
	anio = models.DateField()

	def __unicode__(self):
		return str(self.anio.year)

@python_2_unicode_compatible
class Priorizar(models.Model):
	valor = models.IntegerField()
	criterio = models.ForeignKey(Criterio)
	comunidad = models.ForeignKey(Comunidad)
	capa = models.ForeignKey(Capa)

	def _compo(self):
		return "%s %s" %(self.comunidad, self.porcentaje)

	compo = property(_compo)

	def __str__(self):
		return self.compo