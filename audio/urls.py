from django.urls import path, include
from django.contrib import admin

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('audio_app.urls')),  # redirecting this rout to audio_app
]
