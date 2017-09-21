from django.conf.urls import url
from . import views
from django.views.generic import TemplateView

urlpatterns = [
	url(r'^$', views.index, name='index'),
	url(r'^usuarios/$', views.all_user, name='all_users'),
	url(r'^comunidades/$', views.all_comunities, name='all_comunities'),

]