from django.urls import path
from .views import AddAudioApi, SoundListApi, AudioApi

urlpatterns = [
    path('get_sound_list/<str:file_type>/', SoundListApi.as_view(), name='sound_list_api'),
    path('sound/<str:file_type>/<str:id>/', AudioApi.as_view(), name='sound_api'),
    path('add_sound/', AddAudioApi.as_view(), name='add_sound_api'),
]
