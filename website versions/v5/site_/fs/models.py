from django.db import models
from taggit.managers import TaggableManager
from hitcount.models import HitCountMixin, HitCount
from django.contrib.contenttypes.fields import GenericRelation
from django.utils import timezone
import math
# Create your models here.

from django.contrib.auth.models import User


def whenpublished(self):
        now = timezone.now()
        
        diff= now - self.pub_date

        if diff.days == 0 and diff.seconds >= 0 and diff.seconds < 60:
            seconds= diff.seconds
            
            if seconds == 1:
                return str(seconds) +  "second ago"
            
            else:
                return str(seconds) + " seconds ago"

            

        if diff.days == 0 and diff.seconds >= 60 and diff.seconds < 3600:
            minutes= math.floor(diff.seconds/60)

            if minutes == 1:
                return str(minutes) + " minute ago"
            
            else:
                return str(minutes) + " minutes ago"



        if diff.days == 0 and diff.seconds >= 3600 and diff.seconds < 86400:
            hours= math.floor(diff.seconds/3600)

            if hours == 1:
                return str(hours) + " hour ago"

            else:
                return str(hours) + " hours ago"

        # 1 day to 30 days
        if diff.days >= 1 and diff.days < 30:
            days= diff.days
        
            if days == 1:
                return str(days) + " day ago"

            else:
                return str(days) + " days ago"

        if diff.days >= 30 and diff.days < 365:
            months= math.floor(diff.days/30)
            

            if months == 1:
                return str(months) + " month ago"

            else:
                return str(months) + " months ago"


        if diff.days >= 365:
            years= math.floor(diff.days/365)

            if years == 1:
                return str(years) + " year ago"

            else:
                return str(years) + " years ago"      
     
       

  


STATUS = (
    (0,"Draft"),
    (1,"Publish")
)
section_choice=(("Innovations","Innovations"),("Articles","Articles"),("Reviews","Reviews"),("Gallery","Gallery"))
INNOVATION_CHOICE=((0,"AI"),(1,"robotics"),(2,"electronics"),(3,"vr"),(4,"science"),(5,"startups"),(6,"None"))
alt_text_choice=(("Innovations","Innovations"),("Articles","Articles"),("Reviews","Reviews"),("Gallery","Gallery"),("Events","Events"))
media_choice=(("video","video"),("image","image"),("link","link"))

class Post(models.Model):
    title = models.CharField(max_length=200, unique=True)
    section = models.CharField(max_length=200, unique=True)
   
    innovation_catgry=models.IntegerField(choices=INNOVATION_CHOICE, default=6)      
    
    alt_text= models.CharField(max_length=20,choices=alt_text_choice, blank =False,default="Innovations")
    section = models.CharField(max_length=20,choices=section_choice, blank =False,default="Innovations")
    slug = models.SlugField(max_length=200, unique=True)
    dimage= models.ImageField(upload_to='images/%Y/%m/%d/', blank=False)
    author = models.ForeignKey(User, on_delete= models.CASCADE,related_name='blog_posts')
    updated_on = models.DateTimeField(auto_now= True)
    content = models.TextField()
    event_author = models.CharField(max_length=20,blank =False,default="REPORTER")
    pub_date = models.DateTimeField(auto_now_add= True)
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)
    hit_count_generic = GenericRelation(HitCount, object_id_field='object_pk',
     related_query_name='hit_count_generic_relation')
    tags = TaggableManager()

    def pub(self):
        return whenpublished(self).upper()


    class Meta:
         ordering = ['-created_on']

    def get_absolute_url(self):
        from django.urls import reverse

        return reverse("post_detail", kwargs={"slug": str(self.slug)})
     


class PostImage(models.Model):
    post = models.ForeignKey(Post, default=None, on_delete=models.CASCADE)
    images = models.FileField(upload_to = 'images/')
 
    def __str__(self):
        return self.post.title




    

class Gallery(models.Model):
    title = models.CharField(max_length=200, unique=True)
    alt_text= models.CharField(max_length=20,choices=alt_text_choice, blank =False,default="Innovations")
    media_status=models.CharField(max_length=20,choices=media_choice, blank =False,default="video")
    g_thumb=models.ImageField(upload_to='images/thumb/%Y/%m/%d/',blank=True)
    g_image= models.ImageField(upload_to='images/%Y/%m/%d/',blank=True)
    g_video = models.FileField(upload_to='videos/%Y/%m/%d/',blank=True)
    g_content = models.TextField()
    status = models.IntegerField(choices=STATUS, default=0)
    event_author = models.CharField(max_length=20,blank =False,default="REPORTER")
    pub_date = models.DateTimeField(auto_now_add= True)
    
    created_on = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(max_length=200, unique=True)
    hit_count_generic = GenericRelation(HitCount, object_id_field='object_pk',related_query_name='hit_count_generic_relation')
    youtube_link=models.CharField(max_length=200,blank=True)
    def pub(self):
        return whenpublished(self).upper()

    class Meta:
         ordering = ['-created_on']


    def get_absolute_url(self):
        from django.urls import reverse

        return reverse("gallery_detail", kwargs={"slug": str(self.slug)})
         
	
class Event(models.Model):
    title = models.CharField(max_length=200, unique=True)
    alt_text= models.CharField(max_length=20,choices=alt_text_choice, blank =False,default="Events")
    e_thumb=models.ImageField(upload_to='images/thumb/%Y/%m/%d/')
    e_description = models.TextField()
    location = models.CharField(max_length=200)
    status = models.IntegerField(choices=STATUS, default=0)
    date=models.DateTimeField()
    event_author = models.CharField(max_length=20,blank =False,default="REPORTER")
    pub_date = models.DateTimeField(auto_now_add= True)
    created_on = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(max_length=200, unique=True)

    def pub(self):
        return whenpublished(self).upper()
    
    class Meta:
          ordering = ['-created_on']
    def get_absolute_url(self):
        from django.urls import reverse

        return reverse("event_detail", kwargs={"slug": str(self.slug)})
          



   

    def __str__(self):
         return self.title
    

