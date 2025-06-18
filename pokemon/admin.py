from django.contrib import admin
from .models import Pokemon, Type

class TypeAdmin(admin.ModelAdmin):
    list_display = ('name',)
    filter_horizontal = ('weakTo', 'strongTo')  # Interface pour choisir facilement les relations

class PokemonAdmin(admin.ModelAdmin):
    list_display = ('name',)
    filter_horizontal = ('types',)  # Interface pratique pour associer plusieurs types

admin.site.register(Type, TypeAdmin)
admin.site.register(Pokemon, PokemonAdmin)
