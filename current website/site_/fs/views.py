from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.views import generic
from .models import Post,Gallery,Event
from django.shortcuts import get_object_or_404
from hitcount.models import HitCount
from hitcount.views import HitCountMixin
from itertools import chain
from operator import attrgetter
from hitcount.views import HitCountDetailView

def hello(request):
   return render(request, '/home/vivek/Desktop/we/site_/fs/template/privacy_policy.html', {})


class PostList(generic.ListView):

    queryset = Post.objects.filter(status=1).order_by('-created_on')
    template_name = 'index.html'

class PostDetail(HitCountDetailView):
    all_tabs = Post.tags.all()
    model = Post
    template_name = 'article_temp.html'
    count_hit = True
    def get_context_data(self, **kwargs):
        context = super(PostDetail, self).get_context_data(**kwargs)
        slug = self.kwargs['slug']
        main_post = Post.objects.get(slug=slug)
        # get all related_post and exclude the main post, makes sense that way
        related_posts = Post.objects.filter(tags__name__in=list(main_post.tags.all())).distinct().exclude(slug=slug)[:4]
        # add related_posts to the context
        context['related_posts'] = related_posts[:4]
        return context

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
def about(request):
   return render(request, 'aboutus.html', {})





class IndexView(generic.ListView):
    context_object_name = 'home_list'
    template_name = 'index.html'
    model=Post
    count_hit = True


    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        context['Post'] = [p for p in Post.objects.filter(status=1).all() if p.alt_text == "Innovations"][:5]
        context['Gallery'] = Gallery.objects.all()
        context['Event'] = Event.objects.all()
        context['popular_posts']= Post.objects.filter(status=1).order_by('-hit_count_generic__hits')[:5]
        context['popular_posts_1']= Post.objects.filter(status=1).order_by('-hit_count_generic__hits')[:1]
        context['Gallery_sidebar'] = Gallery.objects.filter(status=1).all()[:4]
        context['Event_sidebar'] = Event.objects.filter(status=1).all()[:4]
        context["total_post"]=sorted(chain(Post.objects.filter(status=1).all(),Gallery.objects.all(), Event.objects.all()),key=attrgetter('created_on'), reverse=True)
        context['Reviews_popular'] = Post.objects.filter(status=1,alt_text='Reviews').order_by('-hit_count_generic__hits')[:5]
        context['Articles_popular'] = Post.objects.filter(status=1,alt_text='Article').order_by('-hit_count_generic__hits')[:5]
        context['intro_post1']=Post.objects.filter(status=1,alt_text='Innovations').order_by('-hit_count_generic__hits')[:1]
        context['intro_post2']= Post.objects.filter(status=1,alt_text='Innovations').order_by('-hit_count_generic__hits')[1:2]
        context['intro_post3']= Post.objects.filter(status=1,alt_text='Innovations').order_by('-hit_count_generic__hits')[2:3]

        # And so on for more models
        return context

