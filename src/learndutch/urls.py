from django.conf.urls.defaults import patterns, include, url
from django.views.generic import TemplateView
from learndutch.mainapp.views import *
from django.conf.urls.static import static
from learndutch import settings

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'learndutch.views.home', name='home'),
    # url(r'^learndutch/', include('learndutch.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    
    url(r'^$', PageView.as_view(), kwargs={'slug':'_home'}, name="home"),
    url(r'^login/$', 'django.contrib.auth.views.login', {'template_name': 'login.html'}),
    url(r'^logout/$', 'django.contrib.auth.views.logout', {'next_page':'/'}),
    url(r'^add-noun/$', CreateNounView.as_view(), name="add-noun"),
    url(r'^add-verb/$', CreateVerbView.as_view(), name="add-verb"),
    url(r'^add-adjective/$', CreateAdjectiveView.as_view(), name="add-adjective"),
    url(r'^add-word/$', CreateWordView.as_view(), name="add-word"),
    url(r'^add-sentence/$', CreateSentenceView.as_view(), name="add-sentence"),
    url(r'^add-tag/$', CreateTagView.as_view(), name="add-tag"),
    url(r'^add-page/$', CreatePageView.as_view(), name='add-page'),
    url(r'^word/(?P<slug>(\w+-?)+)/$', WordView.as_view(), name='search-word'),
    url(r'^word/(?P<slug>(\w+-?)+)/edit/$', UpdateWordView.as_view(), name='update-word'),
    url(r'^words/verbs/$', VerbListView.as_view(), name="verbs"),
    url(r'^words/nouns/$', NounListView.as_view(), name="nouns"),
    url(r'^words/$', WordListView.as_view(), name="words"),
    url(r'^page/(?P<slug>(?=_)(\w+-?)+)/$', HiddenPageView.as_view(), name='hidden-page'),
    url(r'^page/(?P<slug>(\w+-?)+)/$', PageView.as_view(), name='page'),
    url(r'^page/(?P<slug>(\w+-?)+)/edit/$', UpdatePageView.as_view(), name='update-page'),
    url(r'^pages/$', PageListView.as_view(), name='pages'),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
