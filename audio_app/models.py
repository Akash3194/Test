from django.db import models
from django.utils import timezone
from rest_framework.exceptions import ValidationError


def validate_date(date):
    """FUnction to check if given time is not in past"""
    if date < timezone.now().date():
        raise ValidationError("Date cannot be in the past")


class Song(models.Model):
    id = models.AutoField(primary_key=True)
    song_name = models.CharField(max_length=100)
    duration = models.PositiveIntegerField()
    uploaded_time = models.DateField(validators=[validate_date])
    song = models.FileField(upload_to='media/songs/')

    def __str__(self):
        return self.song_name


class Podcast(models.Model):
    id = models.AutoField(primary_key=True)
    podcast_name = models.CharField(max_length=100)
    duration = models.PositiveIntegerField()
    uploaded_time = models.DateField(validators=[validate_date])
    podcast = models.FileField(upload_to='media/podcasts/')
    host = models.CharField(max_length=100)

    # paticipants is a list but i am storing it here comma seperated in MYSQL
    # I am not using MongoDb even NoSql is best for storing arrays inside a field
    # Because We are not searching or filtering for now using participants, we are just storing it
    # all validations will be integrated as written in test pdf
    participants = models.CharField(max_length=1000, blank=True, null=True)

    def __str__(self):
        return self.podcast_name


class AudioBook(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100)
    audio = models.FileField(upload_to='media/audiobooks/')
    author = models.CharField(max_length=100)
    narrator = models.CharField(max_length=100)
    duration = models.PositiveIntegerField()
    uploaded_time = models.DateField(validators=[validate_date])

    def __str__(self):
        return self.title

