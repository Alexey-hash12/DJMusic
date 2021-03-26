from django.db import models
from django.contrib.auth.models import User
from mainapp.models import AuthorModel

class ProfileUserModel(models.Model):
	""" Profile user model """

	STATUS = [
		("SILVER", "SILVER"),
		("GOLD", "GOLD"),
		("PLATINUM", "PLATINUM")
	]
	status = models.CharField(choices=STATUS, default="SILVER", max_length=10)
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	face = models.ImageField(upload_to='user_faces/', null=True)
	subscribers = models.ManyToManyField(AuthorModel)

	def __str__(self):
		return self.user.username

