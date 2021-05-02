from rest_framework import serializers
from rest_framework.exceptions import ValidationError
from .models import Song, Podcast, AudioBook


def val(file_type):
    sound_types = ['song', 'podcast', 'audiobook']
    if file_type not in sound_types:
        raise ValidationError(f"Invalid file type, Avl. options are: {', '.join(sound_types)}")


class SongSerializer(serializers.ModelSerializer):
    class Meta:
        model = Song
        fields = '__all__'


class PodcastSerializer(serializers.ModelSerializer):
    class Meta:
        model = Podcast
        exclude = ['participants']

    def create(self, validated_data):
        """Participant should be a list of arrays so it should be stored in mongo db for better performance
            But for this test case we are not searching or filtering or doing any process which needs participants list
            that is why i am storing participant list a comma separated string and storing in db,
            to make things little easy
        """
        data = validated_data.copy()
        participants = self.initial_data.get('participants')

        if participants:
            if type(participants) != list:
                raise ValidationError({'participants': 'Provide array of participants.'})

            if len(participants) > 10:
                raise ValidationError({"participants": "Only 10 participants are allowed"})

            for name in participants:
                string = ''
                if len(name) > 100:
                    raise ValidationError({"participants": "Any participant string can not exceed 100 characters"})
                string += f"{name} "
            data['participants'] = ', '.join(self.initial_data['participants']).strip()

        print(validated_data)
        obj = Podcast.objects.create(**data)
        return obj


class AudioSerializer(serializers.ModelSerializer):
    class Meta:
        model = AudioBook
        fields = '__all__'


class FileTypeSerializer(serializers.Serializer):
    file_type = serializers.CharField(validators=[val])


class QuerySerializer(FileTypeSerializer):
    id = serializers.IntegerField()
