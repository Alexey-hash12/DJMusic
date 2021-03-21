from django.db import models
from django.contrib.auth.models import User


class MusicModel(models.Model):
	title = models.CharField(max_length=150)
	text = models.TextField()
	file = models.FileField(upload_to='files/music/')
	poster = models.ImageField(upload_to='files/music_poster/')
	date = models.DateTimeField()


	def __str__(self):
		return f"{self.title}"


class AuthorModel(models.Model):
	name = models.CharField(max_length=100)
	surname = models.CharField(max_length=100)
	desc = models.TextField()
	age = models.PositiveIntegerField(default=0)
	music = models.ManyToManyField(MusicModel)
	face = models.ImageField(upload_to='files/authors_face/', null=True)

	def __str__(self):
		return self.name
