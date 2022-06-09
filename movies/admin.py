from pyexpat import model
from django.contrib import admin
from .models import Genre, Movie
# Register your models here.


@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']


@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    list_display = search_fields = ['title']

