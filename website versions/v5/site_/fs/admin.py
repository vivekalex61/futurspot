from django.contrib import admin
from .models import Post ,Gallery,Event




class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'status','created_on')
    list_filter = ("status",)
    search_fields = ['title', 'content']
    prepopulated_fields = {'slug': ('title',)}
  
admin.site.register(Post, PostAdmin)

class GalleryAdmin(admin.ModelAdmin):
    list_display = ('title', 'status','created_on')
    list_filter = ("status",)
#    prepopulated_fields = {'slug': ('title',)}
admin.site.register(Gallery,GalleryAdmin)

class EventAdmin(admin.ModelAdmin):
    list_display = ('title', 'status','created_on')
    list_filter = ("status",)
admin.site.register(Event,EventAdmin)


# Register your models here.
