from django.contrib.sitemaps import Sitemap
from fs.models import Post,Gallery,Event

class PostSitemap(Sitemap):
    changefreq = "always"
    priority = 0.8
    
    def items(self):
        return Post.objects.filter(status=1)

    def lastmod(self, obj):
        return obj.updated_on
        
class GallerySitemap(Sitemap):
    changefreq = "always"
    priority = 0.8
    
    def items(self):
        return Gallery.objects.filter(status=1)

    def lastmod(self, obj):
        return obj.created_on        
        
class EventSitemap(Sitemap):
    changefreq = "always"
    priority = 0.8
    
    def items(self):
        return Event.objects.filter(status=1)

    def lastmod(self, obj):
        return obj.created_on        
