from django.urls import path

from . import views


urlpatterns = [
	path('', views.HomePageView.as_view(), name='home_page'),
	path('music/', views.MusicPageView.as_view(), name='music'),
	path('authors/', views.AuthorsPageView.as_view(), name='authors')
]