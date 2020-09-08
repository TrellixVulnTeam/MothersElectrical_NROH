from django.contrib.sitemaps import Sitemap
from django.shortcuts import reverse

class StaticViewSitemap(Sitemap):
    def item(self):
        return['windex','wAboutUs','wretrailers','wcontactUs']
    def location(self,item):
        return reverse(item)