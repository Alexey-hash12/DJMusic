# Django Views
from django.shortcuts import render, redirect
from django.views.generic.base import View

#datetime
import datetime

# Logging 
import logging

#Models
from .models import MusicModel, AuthorModel

#Email
from .tasks import send_message
logger = logging.getLogger(__name__)

#Cache
from django.core.cache import cache
from django.core.cache.backends.base import DEFAULT_TIMEOUT
from django.conf import settings

CACHE_TTL = getattr(settings, "CACHE_TTL", DEFAULT_TIMEOUT)


# Home Page
class HomePageView(View):
	def get(self, request):
		# if cache.get('author'):
		# 	author = cache.get('author')
		# 	logger.info(f"Getting {author} From cache")
		# else:
		# 	try:
		author = AuthorModel.objects.all().order_by("-id")[0]	
		# 		logger.info(f"Getting {author} From model")
		# 		cache.set('author', author)
		# 	except AuthorModel.DoesNotExist:
		# 		return redirect('/')	

		logger.info(f"Home Page View...(date: {datetime.datetime.now()}),(user: {request.user.username})")
		send_message.delay("alexryzhak238@gmail.com")
		context = {'author':author}
		return render(request, 'mainapp/home_page.html', context)

# Music Page
class MusicPageView(View):
	def get(self, request):
		return render(request, 'mainapp/music_page.html', {})


# Author Page
class AuthorsPageView(View):
	def get(self, request):
		return render(request, 'mainapp/authors_page.html', {})		