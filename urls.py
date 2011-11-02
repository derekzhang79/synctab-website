from django.conf.urls.defaults import patterns, include, url

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('website.views',
    url(r'^$', 'home', name='home'),
    url(r'^download/$', 'download', name='download'),
    url(r'^screenshots/$', 'screenshots', name='screenshots'),
    url(r'^contact/$', 'contact', name='contact'),
    url(r'^submit-issue/$', 'submitIssue', name='submitIssue'),
    url(r'^help/$', 'help', name='help'),
    url(r'^help/getting-started/$', 'getting_started', name='getting_started'),
    url(r'^help/how-to/android-app/$', 'how_to_use_android_app', name='how_to_use_android_app'),
    url(r'^help/how-to/chrome-ext/$', 'how_to_use_chrome_ext', name='how_to_use_chrome_ext'),
    url(r'^sitemap\.xml$', 'sitemap'),
    url(r'^robots\.txt', 'robots'),
)

urlpatterns += patterns('website.mobile',
    url(r'^m/$', 'home', name='m_home'),
    url(r'^m/download/$', 'download', name='m_download'),
    url(r'^m/screenshots/$', 'screenshots', name='m_screenshots'),
    url(r'^m/contact/$', 'contact', name='m_contact'),
    url(r'^m/submit-issue/$', 'submitIssue', name='m_submitIssue'),
    url(r'^m/help/$', 'help', name='m_help'),
    url(r'^m/help/getting-started/$', 'getting_started', name='m_getting_started'),
    url(r'^m/help/how-to/android-app/$', 'how_to_use_android_app', name='m_how_to_use_android_app'),
    url(r'^m/help/how-to/chrome-ext/$', 'how_to_use_chrome_ext', name='m_how_to_use_chrome_ext')
)


#urlpatterns += patterns('',
#    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
#    url(r'^admin/', include(admin.site.urls)),
#)
