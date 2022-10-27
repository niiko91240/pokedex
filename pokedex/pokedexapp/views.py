from django.shortcuts import get_object_or_404, render
from .model.pokemon import Pokemon, Type
from django.http import HttpResponse
from django.template import loader
from asyncio.windows_events import NULL
import requests
import os


# Create your views here.

def insert_api(request):
    text = '<p>Page du script d\insertion des données'


    # ---- INSERTION DES TYPES ----
    # result3 = requests.get("https://pokeapi.co/api/v2/type").json()
    # text = str(result3['results'])
    # for x in result3['results']:
    #     monType = Type()
    #     monType.nom = x['name']
    #     monType.save()


    # ---- INSERTION DES POKEMONS ----
    # result2 = requests.get("https://pokeapi.co/api/v2/pokemon/?limit=151").json()
    # result = requests.get("https://pokeapi.co/api/v2/pokemon/500/").json()

    # text='<h1>Insertion des données de l\'api dans la base de données.</h1>'
    # liste_types = []
    # for poke in result2['results']:
    #     result = requests.get(poke['url']).json()
    #     text +=  "<br> nom : " + str(result['name'])
    #     text +=  "<br> numéro : " + str(result['id'])
    #     text +=  "<br> types : "
    #     text +=  "<br> poids : " + str(result['weight'])
    #     text +=  "<br> taille : " + str(result['height'])
    #     text +=  "<br> points de vie : " + str(result['stats'][0]['base_stat'])
    #     text +=  "<br> attaque : " + str(result['stats'][1]['base_stat'])
    #     text +=  "<br> defense : " + str(result['stats'][2]['base_stat'])
    #     text +=  "<br> special attaque : " + str(result['stats'][3]['base_stat'])
    #     text +=  "<br> special defense : " + str(result['stats'][4]['base_stat'])
    #     text +=  "<br> vitesse : " + str(result['stats'][5]['base_stat'])
    #     text += "<br> image : " + str(result['sprites']['other']['official-artwork']['front_default'])
    #     ajout_pokemon = Pokemon()
    #     ajout_pokemon.nom = result['name']
    #     ajout_pokemon.numero = result['id']
    #     ajout_pokemon.poids = result['weight']
    #     ajout_pokemon.taille = result['height']
    #     ajout_pokemon.pv = result['stats'][0]['base_stat']
    #     ajout_pokemon.attaque = result['stats'][1]['base_stat']
    #     ajout_pokemon.defense = result['stats'][2]['base_stat']
    #     ajout_pokemon.special_attaque = result['stats'][3]['base_stat']
    #     ajout_pokemon.special_defense = result['stats'][4]['base_stat']
    #     ajout_pokemon.vitesse = result['stats'][5]['base_stat']
    #     ajout_pokemon.front_image = result['sprites']['other']['official-artwork']['front_default']
    #     ajout_pokemon.save()
    #     liste_types.clear()
    #     for x in result['types']:
    #         text +=  ' ' + str(x['type']['url'].split("/")[-2])
    #         liste_types.append(x['type']['url'].split("/")[-2])
    #     for x in liste_types:
    #         receive_user = Type.objects.get(id=x)
    #         ajout_pokemon.types.add(receive_user)
    return HttpResponse(text)

def liste(request):
    text = '<h1>Liste des pokemons</h1>'
    text += '<br> ' + str(get_object_or_404(Pokemon, numero=1).nom)
    return HttpResponse(text)