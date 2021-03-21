from django.db import models
from django.contrib.auth.models import User


# Music
class MusicModel(models.Model):
	title = models.CharField(max_length=150)
	text = models.TextField()
	file = models.FileField(upload_to='files/music/')
	poster = models.ImageField(upload_to='files/music_poster/')
	date = models.DateTimeField()

	def __str__(self):
		return self.title


# Album
class AlbumModel(models.Model):
	title = models.CharField(max_length=150)
	music = models.ManyToManyField(MusicModel)
	poster = models.ImageField(upload_to='files/Albums_poster')
	date = models.DateTimeField()

	def __str__(self):
		return self.title


# Author
class AuthorModel(models.Model):
	name = models.CharField(max_length=100)
	surname = models.CharField(max_length=100)
	desc = models.TextField()
	age = models.PositiveIntegerField(default=0)
	music = models.ManyToManyField(MusicModel)
	albums = models.ManyToManyField(AlbumModel)
	face = models.ImageField(upload_to='files/authors_face/', null=True)

	def __str__(self):
		return self.name

