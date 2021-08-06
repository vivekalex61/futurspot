from django.db import models
from taggit.managers import TaggableManager
from hitcount.models import HitCountMixin, HitCount
from django.contrib.contenttypes.fields import GenericRelation

# Create your models here.

from django.contrib.auth.models import User

STATUS = (
    (0,"Draft"),
    (1,"Publish")
)
section_choice=(("Innovations","Innovations"),("Articles","Articles"),("Reviews","Reviews"),("Gallery","Gallery"))
INNOVATION_CHOICE=((0,"AI"),(1,"robotics"),(2,"electronics"),(3,"vr"),(4,"science"),(5,"startups"),(6,"None"))
alt_text_choice=(("Innovations","Innovations"),("Articles","Articles"),("Reviews","Reviews"),("Gallery","Gallery"),("Events","Events"))
media_choice=(("video","video"),("image","image"))

class Post(models.Model):
    title = models.CharField(max_length=200, unique=True)
    section = models.CharField(max_length=200, unique=True)
   
    innovation_catgry=models.IntegerField(choices=INNOVATION_CHOICE, default=4)      
    
    alt_text= models.CharField(max_length=20,choices=alt_text_choice, blank =False,default="Innovations")
    section = models.CharField(max_length=20,choices=section_choice, blank =False,default="Innovations")
    slug = models.SlugField(max_length=200, unique=True)
    dimage= models.ImageField(upload_to='images/%Y/%m/%d/', blank=False)
    author = models.ForeignKey(User, on_delete= models.CASCADE,related_name='blog_posts')
    updated_on = models.DateTimeField(auto_now= True)
    content = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)
    hit_count_generic = GenericRelation(HitCount, object_id_field='object_pk',
     related_query_name='hit_count_generic_relation')
    tags = TaggableManager()
    class Meta:
         ordering = ['-created_on']


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
    created_on = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(max_length=200, unique=True)
    hit_count_generic = GenericRelation(HitCount, object_id_field='object_p',related_query_name='hit_count_generic_relation')
    
    class Meta:
         ordering = ['-created_on']
	
class Event(models.Model):
    title = models.CharField(max_length=200, unique=True)
    alt_text= models.CharField(max_length=20,choices=alt_text_choice, blank =False,default="Events")
    e_thumb=models.ImageField(upload_to='images/thumb/%Y/%m/%d/')
    e_description = models.TextField()
    location = models.CharField(max_length=200)
    status = models.IntegerField(choices=STATUS, default=0)
    date=models.DateTimeField()
    created_on = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(max_length=200, unique=True)
    
    class Meta:
          ordering = ['-created_on']
     
       

  


    def __str__(self):
         return self.title
