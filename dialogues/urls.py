from django.conf.urls import url

from . import views

urlpatterns = [
	url(r'^$', views.index, name = 'index'),
	url(r'hv/$', views.home_visit_index, name = 'home_visit_index'),
	url(r'hv/dist/(?P<district_id>\d+)/$', views.dist_direct_home_visit_index),
	url(r'^ajax_submit_new_home_visit/$', views.ajax_submit_new_home_visit),
	url(r'^ajax_submit_new_guest_invite/$', views.ajax_submit_new_guest_invite),
	url(r'^ajax_get_regions_in_zone/(?P<parent_id>\d+)/$', views.ajax_get_regions_in_zone),
	url(r'^ajax_submit_new_dialogue/$', views.ajax_submit_new_dialogue),
	url(r'^ajax_get_total_count/$', views.ajax_get_total_count),
	url(r'^leaders_dashboard/$', views.leaders_dashboard),
	url(r'^my_activities/$', views.my_activities),
	url(r'^download_entire_dialogue_list/$', views.export_entire_dialogue_list_xls),
	url(r'^download_dialogue_list_date_range/$', views.export_dialogue_list_date_range_xls),
	url(r'^download_per_chapter_dialogue_list_date_range/$', views.export_chapter_dialogue_list_date_range_xls),
	url(r'^ajax_get_chapters_in_region/(?P<parent_id>\d+)/$', views.ajax_get_chapters_in_region),
	url(r'^ajax_get_districts_in_chapter/(?P<parent_id>\d+)/$', views.ajax_get_districts_in_chapter),
	url(r'^ajax_hv_get_district_summary/(?P<district_id>\d+)/$', views.ajax_hv_get_district_summary),
	]
