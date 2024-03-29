from django.urls import path
from django.conf import settings
from client.views import HomeView,ServiceView,CaseView,IndustryView,ContactView,CareersView,ApplyView,AboutView
from django.conf.urls.static import static
from django.contrib.sitemaps import views as sitemap_views
from django.urls import path
from .sitemaps import ServiceSitemap, IndustriesSitemap, CaseStudiesSitemap, JobSitemap

sitemaps = {
    'services': ServiceSitemap,
    'industries': IndustriesSitemap,
    'case_studies': CaseStudiesSitemap,
    'jobs': JobSitemap,
}
urlpatterns = [
    path('',HomeView.as_view(),name="Home",),
    path('service/<slug:name>',ServiceView.as_view(),name="Service"),
    path('case/<slug:name>',CaseView.as_view(),name="Case"),
    path('industry/<slug:name>',IndustryView.as_view(),name="Industry"),
    path('contact/',ContactView.as_view(),name="Contact"),
    path('careers/',CareersView.as_view(),name="Careers"),
    path('careers/apply/<slug:name>',ApplyView.as_view(),name="Apply"),
    path('about/',AboutView.as_view(),name="About"),
    path('sitemap.xml', sitemap_views.sitemap, {'sitemaps': sitemaps}, name='django.contrib.sitemaps.views.sitemap'),
]
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
