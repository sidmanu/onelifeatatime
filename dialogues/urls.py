from django.conf.urls import url

from . import views

urlpatterns = [
	url(r'^$', views.index, name = 'index'),
	url(r'^ajax_get_regions_in_zone/(?P<parent_id>\d+)/$', views.ajax_get_regions_in_zone),
	url(r'^submit_new_dialogue/$', views.submit_new_dialogue),
	url(r'^leaders_dashboard/$', views.leaders_dashboard),
	url(r'^ajax_get_chapters_in_region/(?P<parent_id>\d+)/$', views.ajax_get_chapters_in_region),
	url(r'^ajax_get_districts_in_chapter/(?P<parent_id>\d+)/$', views.ajax_get_districts_in_chapter),
	]
