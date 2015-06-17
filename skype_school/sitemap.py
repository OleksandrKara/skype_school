# -*- coding: utf-8 -*-
# ����������� ������� �����
from django.contrib.sitemaps import Sitemap
from skype_school.articles.models import Post

class SitemapArticlesXML(Sitemap):
    # ������� ���������� �������� (��. http://www.sitemaps.org/) 
    changefreq = 'weekly'
    # ��������� ������������ �������� (��. http://www.sitemaps.org/)
    priority = 0.5
	
	def items(self):
        # �������� �� ��������� ������ �� ������ ��� ������� ����������
        # ��������� ���� sitemap
        return Post.objects.all()
	
	def lastmod(self, obj):
        # ����� ���������� ���� ������� ����������� � ��������� lastmod
        # (��. http://www.sitemaps.org/)
        return obj.modified
	
	def location(self, obj):
		return "/articles/%s/" % obj.slug

class StaticViewSitemap(Sitemap):
    priority = 0.5
    changefreq = 'daily'
    def items(self):
        return ['index']

    def location(self, item):
        return reverse(item)

'''class SitemapXML(Sitemap):
    # ������� ���������� �������� (��. http://www.sitemaps.org/) 
    changefreq = 'weekly'
    # ��������� ������������ �������� (��. http://www.sitemaps.org/)
    priority = 0.5

    def items(self):
        # �������� �� ��������� ������ �� ������ ��� ������� ����������
        # ��������� ���� sitemap
        return Foto.objects.filter(date__lte='2055-01-01').order_by('id')
		#date__lte='2055-01-01'

    def lastmod(self, obj):
        # ����� ���������� ���� ������� ����������� � ��������� lastmod
        # (��. http://www.sitemaps.org/)
        return obj.date

    def location(self, obj):
        # ����� ���������� URL ������� ����������� � ��������� loc
        # (��. http://www.sitemaps.org/)
        return "/media/%s" % obj.image_location'''
		
class FlatpageSitemap(Sitemap): 
    def items(self): 
        from django.contrib.sites.models import Site 
        return FlatPage.all().filter('sites = ', Site.objects.get_current().key()) 