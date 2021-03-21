from rest_framework import serializers
from mainapp.models import MusicModel, AuthorModel, AlbumModel

class MusicSerializer(serializers.ModelSerializer):
	class Meta:
		model = MusicModel
		fields = "__all__"


class Albumserializer(serializers.ModelSerializer):
	class Meta:
		model = AlbumModel
		fields = "__all__"



class AuthorSerializer	(serializers.ModelSerializer):
	class Meta:
		model = AuthorModel
		fields = "__all__"
	