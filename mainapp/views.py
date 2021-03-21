# Django Views
from django.shortcuts import render, redirect
from django.views.generic.base import View

#datetime
import datetime

# Logging 
import logging

#Models
from .models import MusicModel

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
		if cache.get('musics'):
			musics = cache.get('musics')
			logger.info("From cache")
		else:
			try:
				musics = MusicModel.objects.all()	
				logger.info("From model")
				cache.set('musics', musics)
			except MusicModel.DoesNotExist:
				return redirect('/')	

		logger.info(f"Home Page View...(date: {datetime.datetime.now()}")
		# send_message.delay("alexryzhak238@gmail.com")
		return render(request, 'mainapp/home_page.html', {'musics':musics})