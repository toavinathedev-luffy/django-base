from django.shortcuts import render
from .models import Pokemon

def home(request):
    # Afficher 2 pokemons max au départ
    pokemons = Pokemon.objects.all()[:2]
    return render(request, 'index.html', {'pokemons': pokemons})

def pokemon_list(request):
    # Afficher tous les pokemons
    pokemons = Pokemon.objects.all()
    return render(request, 'index.html', {'pokemons': pokemons})
