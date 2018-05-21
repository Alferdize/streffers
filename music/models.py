from django.db import models
from django.urls import reverse

# Create your models here.

class Album(models.Model):
    artist = models.CharField(max_length=250)
    album_title = models.CharField(max_length=500)
    genre = models.CharField(max_length=100)
    album_logo = models.FileField()

    def get_absolute_url(self):
        return reverse('music:detail',kwargs = {'pk' : self.pk} )
    
    def __str__(self):
        return self.album_title + '-' + self.artist
    
 
class Songs(models.Model):
    artist = models.ForeignKey(Album, on_delete = models.CASCADE)
    song_title = models.CharField(max_length=250)
    file_type = models.CharField(max_length=10)
    is_favorite = models.BooleanField(default=False)


    def __str__(self):
        return self.song_title
 
