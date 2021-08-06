from . import views
from django.urls import path
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from django.conf.urls import  include, url
from django.conf.urls.static import static
from django.conf import settings

from django.contrib.sitemaps.views import sitemap
from fs.sitemaps import PostSitemap,GallerySitemap,EventSitemap

sitemaps = {
    "posts": PostSitemap,"Gallery":GallerySitemap,"Event":EventSitemap,
}

urlpatterns = [
 #   path('',views.PostList.as_view(), name='home'),
    path('',views.IndexView.as_view(),name="home_list"),
  
    path('<slug:slug>/', views.PostDetail.as_view(), name='post_detail'),
    path('gd/<slug:slug>/', views.gallerydetail.as_view(), name='gallery_detail'),
    path('td/<slug:slug>/', views.techeventdetail.as_view(), name='event_detail'),
    path('ai_section', views.AItemp.as_view(),name='ait'),
    path('electronics_section', views.eltemp.as_view(),name='elt'),
    path('robotics_section', views.rotemp.as_view(),name='rbt'),
    path('science_section', views.scitemp.as_view(),name='sct'),
    path('vr_section', views.vrtemp.as_view(),name='vrt'),
    path('pp_section', views.pps , name='privacy_policy'),
    path('termsandservices', views.terms , name='termsofservices'),
    path('contactus', views.contact , name='contactus'),
    path('aboutus', views.about , name='aboutus'),
    path('reviews', views.reviews.as_view(),name='ait'),
    path('articles', views.articles.as_view(),name='ait'),
    path('tech_events', views.tech_events.as_view(),name='ait'),
    path('startups', views.startups.as_view(),name='ait'),  
    path('gallery', views.gallery.as_view(),name='ait'),  
    path("sitemap.xml", sitemap, {"sitemaps": sitemaps}, name="sitemap"),



]
urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
urlpatterns +=static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
