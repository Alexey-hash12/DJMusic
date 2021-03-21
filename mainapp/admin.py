from django.contrib import admin

from .models import MusicModel, AuthorModel


admin.site.register(MusicModel)
admin.site.register(AuthorModel)