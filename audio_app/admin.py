from django.contrib import admin
from .models import Song, Podcast, AudioBook

# Register your models here.
admin.site.register([Song, Podcast, AudioBook])