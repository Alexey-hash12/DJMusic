from django.shortcuts import render
from rest_framework import viewsets
from mainapp.models import MusicModel, AuthorModel, AlbumModel
from .serializers import MusicSerializer, AuthorSerializer, Albumserializer

class MusicsViewSet(viewsets.ModelViewSet):
	queryset = MusicModel.objects.all()
	serializer_class = MusicSerializer


class AuthorsViewSet(viewsets.ModelViewSet):
	queryset = AuthorModel.objects.all()	
	serializer_class = AuthorSerializer

class AlbumsViewSet(viewsets.ModelViewSet):
	queryset = AlbumModel.objects.all()
	serializer_class = Albumserializer