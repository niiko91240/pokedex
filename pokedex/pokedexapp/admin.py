from django.contrib import admin
from .models import Pokemon, Type, Equipe

# Register your models here.
admin.site.register(Pokemon)
admin.site.register(Type)
admin.site.register(Equipe)