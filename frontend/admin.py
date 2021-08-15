from django.contrib import admin
from .models import Event, Blog, Podcast, Product
# Register your models here.


class EventAdmin(admin.ModelAdmin):
    list_display = ('id', 'season', 'month', 'name', 'details', 'betting', 'created_at', 'updated_at')
admin.site.register(Event)

class BlogAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'header', 'blog', 'image', 'url', 'created_at', 'updated_at')
admin.site.register(Blog)

class PodcastAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'description', 'episode', 'video', 'created_at', 'updated_at']
admin.site.register(Podcast)

class ProductAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'description', 'price', 'image', 'colors', 'types', 'sex', 'sizes', 'quantity', 'created_at', 'updated_at']
admin.site.register(Product)