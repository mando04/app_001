from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'untitled.views.home', name='home'),
    url(r'^www/', include('www.urls')),

    url(r'^admin/', include(admin.site.urls)),
)
