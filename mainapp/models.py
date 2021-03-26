from django.db import models
from django.contrib.auth.models import User


class Category(models.Model):
	""" Category """

	title = models.CharField(max_length=100)



class MusicModel(models.Model):
	""" Music model """

	STATUS = [
		("SILVER", "SILVER"),
		("GOLD", "GOLD"),
		("PLATINUM", "PLATINUM")
	]

	title = models.CharField(max_length=150)
	text = models.TextField()
	file = models.FileField(upload_to='files/music/')
	poster = models.ImageField(upload_to='files/music_poster/')
	date = models.DateTimeField()
	status = models.CharField(choices=STATUS, default='SILVER', max_length=20, null=True)

	def __str__(self):
		return self.title


class AlbumModel(models.Model):
	""" Album model """

	STATUS = [
		("SILVER", "SILVER"),
		("GOLD", "GOLD"),
		("PLATINUM", "PLATINUM")
	]

	title = models.CharField(max_length=150)
	music = models.ManyToManyField(MusicModel)
	desc = models.TextField(null=True)
	poster = models.ImageField(upload_to='files/Albums_poster')
	date = models.DateTimeField()
	status = models.CharField(choices=STATUS, default='SILVER', max_length=20, null=True)
	draft = models.BooleanField(default=False, null=True)

	def __str__(self):
		return self.title


class AuthorModel(models.Model):
	""" Author model """

	name = models.CharField(max_length=100)
	surname = models.CharField(max_length=100)
	desc = models.TextField()
	age = models.PositiveIntegerField(default=0)
	music = models.ManyToManyField(MusicModel)
	albums = models.ManyToManyField(AlbumModel)
	face = models.ImageField(upload_to='files/authors_face/', null=True)

	def __str__(self):
		return self.name

