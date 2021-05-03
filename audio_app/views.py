from rest_framework.generics import GenericAPIView
from rest_framework.mixins import ListModelMixin, DestroyModelMixin, RetrieveModelMixin, CreateModelMixin, \
    UpdateModelMixin
from .serializers import *


class BaseClass(GenericAPIView):
    """
    This class contains two methods which are used in every api
    These wil be inherited
    One of the method provides serializer according to file type sent through request
    Other method provides queryset according to file type sent through request
    """
    def get_serializer_class(self):
        models_mapping = {'song': SongSerializer, "podcast": PodcastSerializer, "audiobook": AudioSerializer}
        return models_mapping[self.kwargs['file_type']]

    def get_queryset(self):
        models_mapping = {'song': Song, "podcast": Podcast, "audiobook": AudioBook}
        queryset = models_mapping[self.kwargs['file_type']].objects.all()
        return queryset


def check_inputs(ser, data_, param_list):
    """
    This function is called in every class below
    It validates the most common data: file_type and id
    """
    print(data_)
    if 'file_type' not in data_:
        raise ValidationError({"file_type": "file_type is required"})
    data = {param: data_[param] for param in param_list}
    serializer = ser(data=data)
    serializer.is_valid(raise_exception=True)


class AudioApi(BaseClass, RetrieveModelMixin, UpdateModelMixin, DestroyModelMixin):
    """
    This class consists if 3 api's, retreiving, deleting and updating a track record
    """

    lookup_url_kwarg = 'id'

    def get(self, request, file_type, id):
        check_inputs(QuerySerializer, self.kwargs, ['file_type', 'id'])
        return self.retrieve(request)

    def put(self, request, file_type, id):
        check_inputs(QuerySerializer, self.kwargs, ['file_type', 'id'])
        return self.update(request)

    def delete(self, request, file_type, id):
        check_inputs(QuerySerializer, self.kwargs, ['file_type', 'id'])
        return self.destroy(request)


class AddAudioApi(GenericAPIView, CreateModelMixin):
    """
    This class creates an api which is used to add new song in database
    """

    def get_serializer_class(self):
        models_mapping = {'song': SongSerializer, "podcast": PodcastSerializer, "audiobook": AudioSerializer}
        return models_mapping[self.request.data['file_type']]

    def post(self, request):
        check_inputs(FileTypeSerializer, request.data, ['file_type'])
        return self.create(request)


class SoundListApi(ListModelMixin, BaseClass):
    """
    This class consist of an Api which is used to list all the tracks in database
    """

    def get(self, request, file_type):
        check_inputs(FileTypeSerializer, self.kwargs, ['file_type'])
        return self.list(request)
