from django.shortcuts import render
from rest_framework import viewsets
from mainapp.models import MusicModel
from .serializers import MusicSerializer

class MusicViewSet(viewsets.ModelViewSet):
	queryset = MusicModel.objects.all()
	serializer_class = MusicSerializer