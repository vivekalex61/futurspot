from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.views import generic
from .models import Post,Gallery,Event


def hello(request):
   return render(request, '/home/vivek/Desktop/we/site_/fs/template/privacy_policy.html', {})


class PostList(generic.ListView):
    queryset = Post.objects.filter(status=1).order_by('-created_on')
    template_name = 'index.html'

class PostDetail(generic.DetailView):
    model = Post
    template_name = 'article_temp.html'
    
class gallerydetail(generic.DetailView):
    model = Gallery
    template_name = 'gallery-detail.html'
    
class techeventdetail(generic.DetailView):
    model = Event
    template_name = 'techevent_detail.html'    
    
class AItemp(generic.ListView):
    queryset = Post.objects.filter(status=1).order_by('-created_on')
    template_name = 'ai_section.html'
    
class eltemp(generic.ListView):
    queryset = Post.objects.filter(status=1).order_by('-created_on')
    template_name = 'electronics_section.html'
  
class vrtemp(generic.ListView):
    queryset = Post.objects.filter(status=1).order_by('-created_on')
    template_name = 'vr_section.html'
class rotemp(generic.ListView):
    queryset = Post.objects.filter(status=1).order_by('-created_on')
    template_name = 'robotics_section.html'
       
class scitemp(generic.ListView):
    queryset = Post.objects.filter(status=1).order_by('-created_on')
    template_name = 'science_section.html'
    
class reviews(generic.ListView):
    queryset = Post.objects.filter(status=1).order_by('-created_on')
    template_name = 'reviews.html'    
class articles(generic.ListView):
    queryset = Post.objects.filter(status=1).order_by('-created_on')
    template_name = 'articles.html'      
class tech_events(generic.ListView):
    queryset = Event.objects.filter(status=1).order_by('-created_on')
    template_name = 'techevents.html'   
class startups(generic.ListView):
    queryset = Post.objects.filter(status=1).order_by('-created_on')
    template_name = 'startups.html'   
class gallery(generic.ListView):
    queryset = Gallery.objects.filter(status=1).order_by('-created_on')
    template_name = 'videos.html'   
    
    
def pps(request):
   return render(request, 'privacy_policy.html', {})
   
def terms(request):
   return render(request, 'terms and services.html', {})
   
def contact(request):
   return render(request, 'contactus.html', {})
    
 
                  
