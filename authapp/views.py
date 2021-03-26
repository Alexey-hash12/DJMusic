from django.shortcuts import render
from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic.base import View
from django.views.generic import CreateView
from django.urls import reverse_lazy
from .forms import AuthUserLoginForm, AuthUserRegisterForm
from django.contrib.auth import authenticate, login
from .models import ProfileUserModel


class AuthRegisterUserView(CreateView):
	""" Register View """

	form_class = AuthUserRegisterForm
	success_url = reverse_lazy('home_page')
	template_name = 'authapp/register_page.html'

	def form_valid(self, form):
		form_valid = super().form_valid(form) # регистрация
		username = form.cleaned_data['username'] # связующее звено из бд
		password = form.cleaned_data['password'] #
		aut_user = authenticate(username=username, password=password) # аутентификация
		login(self.request, aut_user) # авторизация
		return form_valid


# Registration
class AuthLoginUserView(LoginView):
	form_class = AuthUserLoginForm
	template_name = 'authapp/login_page.html'
	success_url = reverse_lazy("home_page")



# Logout
class AuthLogoutUserView(LogoutView):
	next_page = reverse_lazy("home_page")


class ProfileUserView(View):
	def get(self, request, id):
		profile = ProfileUserModel.objects.get(user__id=id)
		context = {'profile': profile}
		return render(request, 'authapp/profile_page.html', context)