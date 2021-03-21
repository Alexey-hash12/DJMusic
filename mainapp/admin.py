from django.contrib import admin

from .models import MusicModel, AuthorModel, AlbumModel


admin.site.register(MusicModel)
admin.site.register(AuthorModel)
admin.site.register(AlbumModel)