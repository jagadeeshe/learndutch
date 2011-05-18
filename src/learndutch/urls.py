from django.conf.urls.defaults import patterns, include, url
from django.views.generic import TemplateView

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'learndutch.views.home', name='home'),
    # url(r'^learndutch/', include('learndutch.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
    
    url(r'^$', TemplateView.as_view(template_name="index.html")),
    url(r'^word/add-noun/$', 'mainapp.views.add_noun'),
    url(r'^word/add-verb/$', 'mainapp.views.add_verb'),
)
