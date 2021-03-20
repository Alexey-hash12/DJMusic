from django.shortcuts import render
from django.views.generic.base import View


# Home Page
class HomePageView(View):
	def get(self, request):
		return render(request, 'mainapp/home_page.html', {})