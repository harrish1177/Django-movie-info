from django.contrib import admin
from .models import Actors, Movies, MovieCast

# Registering my models here.
admin.site.register(Actors)
admin.site.register(Movies)
admin.site.register(MovieCast)

