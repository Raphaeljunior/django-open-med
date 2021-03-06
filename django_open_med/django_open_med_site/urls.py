from django.conf.urls import patterns, include, url
from django.conf import settings
from django.contrib import admin, auth
from django.views.generic import *
from filebrowser.sites import site
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^grappelli/', include('grappelli.urls')),
    url(r'^admin/filebrowser/', include(site.urls)),
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^admin/django-ses/', include('django_ses.urls')),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    #url(r'^form-creator/', include(form_creator_admin_site.urls)),
    url(r'^forms/', include(include('form_designer.urls'))),
    url(r'^/', TemplateView.as_view(template_name="index.html")),
    url(r'^accounts/', include('allauth.urls')),
)

urlpatterns += patterns('patient_client_staff.views',
)

urlpatterns += patterns('dashboard.views',
)

urlpatterns += patterns('portal.views',
    url(r'^portal/login/$', TemplateView.as_view(template_name="login.html")),
)

urlpatterns += patterns('django.contrib.auth.views',
    url(r'^logout/$', 'logout', {'next_page': '/'}, name='portal_logout'),
)
