from django.urls import path

from . import views


urlpatterns = [
	# Authorization
	path('login/', views.AuthLoginUserView.as_view(), name='login'),
	# Registration
	path('register/', views.AuthRegisterUserView.as_view(), name='register'),
	# Logout
	path('logout', views.AuthLogoutUserView.as_view(), name='logout'),
	# Profile
	path('profile/<int:id>', views.ProfileUserView.as_view(), name='profile')

]