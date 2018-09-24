import json

import os
from django.conf import settings
from django.conf.urls import include, url
from django.contrib import admin
from django.http import JsonResponse
from django.shortcuts import render
import urllib.request

# from django.views import generic
# from material.frontend import urls as frontend_urls
# from report_builder import urls as report_builder_urls
from django.conf.urls.static import static
from django.urls import path
from rest_framework.decorators import api_view
from rest_framework.response import Response
from scrapersite import __version__ as scrapersite_version
# from portalcrawler import __version__ as portalcrawler_version
from django.utils.translation import gettext as _


# # from portalcrawler import __version__ as portalcrawler_version
# from django.views.static import serve


@api_view(['get'])
def about(request):
    try:
        application_manifest = json.load(
            open(os.path.join(settings.STATIC_ROOT, '..', 'frontend', 'manifest.json'), mode='r'))
    except FileNotFoundError as e:
        application_manifest = dict()

    return Response(
        dict(
            scrapersite=scrapersite_version,
            portalcrawler='0.0.0',
            application=application_manifest.get('version', '0.0.0')
        )
    )


@api_view(['get'])
def applications(request):
    return Response([
        dict(
            name='Jupyter Notebooks',
            url='https://hegedus3.pikotera.net:8000/user/adcobo/lab?'
        ),
        dict(
            name='Splash server',
            url='http://hegedus3.pikotera.net:8050/'
        ),
        dict(
            name='Scrapy daemon',
            url='http://hegedus3.pikotera.net:6800/'
        )
    ])


admin.site.site_header = 'Adcobo'
admin.site.index_title = _('Site administration')

urlpatterns = [
    # url('^$', generic.RedirectView.as_view(url='./mdm/'), name="index"),
    # url(r'^report_builder/', include(report_builder_urls)),
    # Include Material frontend
    # url(r'', include(frontend_urls)),
    # Include cubesviewer URLs
    # url(r'^cubesviewer/', include('cubesviewer.urls')),

    url(r'^about/', about, name='about'),
    url(r'^applications/', applications, name='applications'),
    # url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),

    url(r'^rest-auth/', include('rest_auth.urls')),
    url(r'^rest-auth/registration/', include('rest_auth.registration.urls')),

    # Admin site and documentation
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^admin/', admin.site.urls),

    # Static
    # url(r'^static/(.*)$', serve, {'document_root': settings.STATIC_ROOT}),

    # url(r'', include('hydra_presentation.urls'), name='presentation'),
    # url(r'^bot/', include('bot.urls'), name='bot'),
    path('notebook/', include('hydra_notebook.urls')),
    url(r'^engine/', include('engine.urls'), name='engine'),
    url(r'^datastore/', include('hydra_datastore.urls'), name='datastore'),
    url(r'^mdm/', include('mdm.urls'), name='mdm'),
]

if settings.DEBUG:
    import debug_toolbar

    urlpatterns += [
        url(r'^__debug__/', include(debug_toolbar.urls))
    ]
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
