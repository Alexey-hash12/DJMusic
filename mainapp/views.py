# Django Views
from django.shortcuts import render, redirect
from django.views.generic.base import View

#datetime
import datetime

# settings
from django.conf import settings

# Logging 
import logging
logger = logging.getLogger(__name__)

#Models
from .models import MusicModel, AuthorModel, AlbumModel

#Email
from .tasks import send_message

#Cache
from django.core.cache import cache
from django.core.cache.backends.base import DEFAULT_TIMEOUT
from django.conf import settings

CACHE_TTL = getattr(settings, "CACHE_TTL", DEFAULT_TIMEOUT)


# Main Views
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
		# send_message.delay("alexryzhak238@gmail.com")
		context = {'author':author}
		template_name = 'mainapp/home_page.html'
		return render(request, template_name, context)

# About Us Page
class AboutUsPageView(View):
	def get(self, request):
		template_name = 'mainapp/about-us_page.html'
		context = {}
		return render(request, template_name, context)

# Contact Page
class ContactPageView(View):
	def post(self, request):
		receiver = settings.EMAIL_HOST_USER
		_, name, sender, theme, message = (tuple(request.POST.values()))
		send_message.delay(name, sender, receiver, theme, message)
		logger.info(f"Getting post request from Contact page user: {request.user} value {request.POST}")
		return redirect('/')
	def get(self, request):
		template_name = 'mainapp/contact_page.html'
		context = {}
		return render(request, template_name, context)

# Music Views
# Music Page
class MusicPageView(View):
	def get(self, request, id=None):
		music = MusicModel.objects.get(id=id)
		context = {'music': music}
		template_name = 'mainapp/music_page.html'
		return render(request, template_name, context)


class AuthorsPageView(View):
	""" Author page view """

	def get(self, request):
		authors = AuthorModel.objects.all()
		context = {'authors': authors}
		return render(request, 'mainapp/authors_page.html', context)		

class AuthorPageView(View):
	""" Author Page View """
	
	def get(self, request, id):
		author = AuthorModel.objects.get(id=id)
		context = {'author': author}
		return render(request, "mainapp/author_page.html", context)

# Album Page
class AlbumDescPageView(View):
	def get(self, request, id):
		queryset = AlbumModel.objects.get(id=id)
		context = {'album': queryset}
		return render(request, 'mainapp/album_desc.html', context)
