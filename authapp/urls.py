from django.urls import path

from . import views


urlpatterns = [
	# Authorization
	path('login/', views.AuthLoginView.as_view(), name='login'),
	# Registration
	path('register/', views.AuthRegisterView.as_view(), name='register'),
	# Logout
	path('logout', views.AuthLogoutView.as_view(), name='logout')
]