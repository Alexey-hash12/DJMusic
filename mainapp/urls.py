from django.urls import path

from . import views


urlpatterns = [
	# Main View
	path('', views.HomePageView.as_view(), name='home_page'),
	path('about-us/', views.AboutUsPageView.as_view(), name='about-us'), 
	path('contact/', views.ContactPageView.as_view(), name='contact'),
	# Music
	path('music/<int:id>', views.MusicPageView.as_view(), name='music'),
	path('all_authors/', views.AuthorsPageView.as_view(), name='authors'),
	path('author/<int:id>', views.AuthorPageView.as_view(), name='author'),
	path('album_desc/<int:id>/', views.AlbumDescPageView.as_view(), name='album_desc')
]