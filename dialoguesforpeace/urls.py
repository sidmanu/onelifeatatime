from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'dialoguesforpeace.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
	url(r'hv/$', 'dialogues.views.home_visit_index', name = 'home_visit_index'),

	url(r'hv/dist/(?P<district_id>\d+)/$', 'dialogues.views.dist_direct_home_visit_index'),
	url(r'^$', 'dialogues.views.index', name='index'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^dialogues/', include('dialogues.urls')),
	url(r'^login/$', 'dialogues.views.login_user'),	
	url(r'^logout/$', 'dialogues.views.logout_user'),	
)
