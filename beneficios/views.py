from django.shortcuts import render

from django.contrib.auth.decorators import login_required
from django.core import serializers
from django.core.urlresolvers import reverse
from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic import TemplateView
from .models import *
from django.db.models import Count


from django.contrib.auth.models import User

# Create your views here.
def index(request):
	return render(request, 'index.html')

def all_user(request):
	data = User.objects.all()
	perfil = Perfil.objects.all()
	sexo = Sexo.objects.all()
	numu = data.count()
	return render(request, 'all_users.html', {'data':data,'perfil': perfil, 'numu':numu, 'sexo':sexo})

def all_comunities(request):
	comunidad = Comunidad.objects.all()
	numc = comunidad.count()
	municipio = Municipio.objects.all()
	return render(request, 'all_comunities.html', {'data':comunidad, 'numc':numc, 'muni': municipio})