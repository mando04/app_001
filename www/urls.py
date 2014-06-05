from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'www.views.home', name='blog-home'),
    url(r'post$', 'www.views.post', name='blog-post'),
    url(r'about$', 'www.views.about', name='blog-about'),
)
