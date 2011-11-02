from django.conf.urls.defaults import patterns, include, url

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('website.views',
    # Examples:
    url(r'^$', 'home', name='home'),
    url(r'^download/$', 'download', name='download'),
    url(r'^screenshots/$', 'screenshots', name='screenshots'),
    url(r'^contact/$', 'contact', name='contact'),
    url(r'^submit-issue/$', 'submitIssue', name='submitIssue'),
    url(r'^help/$', 'help', name='help'),
    url(r'^help/getting-started/$', 'getting_started', name='getting_started'),
    url(r'^help/how-to/android-app/$', 'how_to_use_android_app', name='how_to_use_android_app'),
    url(r'^help/how-to/chrome-ext/$', 'how_to_use_chrome_ext', name='how_to_use_chrome_ext'),


    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)
