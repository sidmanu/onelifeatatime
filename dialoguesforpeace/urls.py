from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'dialoguesforpeace.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

	url(r'^$', 'dialogues.views.index', name='index'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^dialogues/', include('dialogues.urls')),
	url(r'^login/$', 'dialogues.views.login_user'),	
)
