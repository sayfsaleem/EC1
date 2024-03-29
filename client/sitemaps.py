from django.contrib.sitemaps import Sitemap
from .models import Service, Industries, CaseStudies, Job

class ServiceSitemap(Sitemap):
    changefreq = 'weekly'
    priority = 0.9

    def items(self):
        return Service.objects.all()

class IndustriesSitemap(Sitemap):
    changefreq = 'weekly'
    priority = 0.8

    def items(self):
        return Industries.objects.all()

class CaseStudiesSitemap(Sitemap):
    changefreq = 'weekly'
    priority = 0.7

    def items(self):
        return CaseStudies.objects.all()

class JobSitemap(Sitemap):
    changefreq = 'weekly'
    priority = 0.6

    def items(self):
        return Job.objects.all()
