from django.contrib import admin
from django.contrib.auth.models import User, Group

from movies.models import Movie, Actor, Genre

admin.site.unregister(User)
admin.site.unregister(Group)

admin.site.register(Movie)
admin.site.register(Actor)
admin.site.register(Genre)
