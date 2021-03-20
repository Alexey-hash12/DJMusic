from django.shortcuts import render
from django.views.generic.base import View

class ChatPageView(View):
	def get(self, request):
		return render(request, 'chatapp/chat_page.html', {})