from django.contrib import admin
from .models import Genre, Series


class GenreAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')


class SeriesAdmin(admin.ModelAdmin):
    list_display = ('title', 'ratings')


admin.site.register(Genre, GenreAdmin)
admin.site.register(Series, SeriesAdmin)
