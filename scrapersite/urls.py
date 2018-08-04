from django.conf import settings
from django.conf.urls import include, url
from django.shortcuts import render
# from django.views import generic
# from material.frontend import urls as frontend_urls
# from report_builder import urls as report_builder_urls
from django.conf.urls.static import static
from scrapersite import __version__ as scrapersite_version
# # from portalcrawler import __version__ as portalcrawler_version
# from django.views.static import serve


def about(request):
    return render(
        request=request,
        context={
            'scrapersite': scrapersite_version,
            # 'portalcrawler': portalcrawler_version
        },
        template_name='about.html'
    )


urlpatterns = [
    # url('^$', generic.RedirectView.as_view(url='./mdm/'), name="index"),
    # url(r'^report_builder/', include(report_builder_urls)),
    # Include Material frontend
    # url(r'', include(frontend_urls)),
    # Include cubesviewer URLs
    # url(r'^cubesviewer/', include('cubesviewer.urls')),

    # url(r'^about/', about, name='about'),
    # url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))

    # Admin site and documentation
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    # url(r'^admin/', include(admin.site.urls)),

    # Static
    # url(r'^static/(.*)$', serve, {'document_root': settings.STATIC_ROOT}),

    url(r'', include('hydra_presentation.urls'), name='presentation'),
]

if settings.DEBUG:
    import debug_toolbar

    urlpatterns += [
        url(r'^__debug__/', include(debug_toolbar.urls))
    ]
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
