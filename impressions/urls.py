from django.conf.urls import patterns, include, url

import django.contrib.admin as admin

admin.autodiscover()
urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'impapp.views.home', name='home'),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)
