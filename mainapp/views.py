from django.shortcuts import render
from django.views.generic.base import View
import logging

logger = logging.getLogger(__name__)

# Home Page
class HomePageView(View):
	def get(self, request):
		logger.info(f"{request}")
		return render(request, 'mainapp/home_page.html', {})