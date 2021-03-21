from django.shortcuts import render
from django.views.generic.base import View

# Logging 
import logging

#Email
from .tasks import send_message


logger = logging.getLogger(__name__)

# Home Page
class HomePageView(View):
	def get(self, request):
		logger.info(f"{request}")
		send_message.delay("alexryzhak238@gmail.com")
		return render(request, 'mainapp/home_page.html', {})