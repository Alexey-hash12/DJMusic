from django.shortcuts import render

from django.views.generic.base import View


# Authorization
class AuthLoginView(View):
	def get(self, request):
		template_name = 'auth/login_page.html'
		return render(request, template_name, {})
	


# Registration
class AuthRegisterView(View):
	template_name = 'auth/register_page.html'
	pass


# Logout
class AuthLogoutView(View):
	pass
