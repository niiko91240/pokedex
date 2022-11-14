from urllib.request import Request
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
    pokemons_liste = Pokemon.objects.all()
    max_pv = 0
    max_attaque = 0
    max_defense = 0
    max_vitesse = 0
    max_sattaque = 0
    max_sdefense = 0
    for poke in pokemons_liste:
        if(max_pv<poke.pv):
            max_pv = poke.pv
        if(max_attaque<poke.attaque):
            max_attaque = poke.attaque
        if(max_defense<poke.defense):
            max_defense = poke.defense
        if(max_vitesse<poke.vitesse):
            max_vitesse = poke.vitesse
        if(max_sattaque<poke.special_attaque):
            max_sattaque = poke.special_attaque
        if(max_sdefense<poke.special_defense):
            max_sdefense = poke.special_defense
    text += "<br>MAX PV : " + str(max_pv)
    text += "<br>MAX Attaque : " + str(max_attaque)
    text += "<br>MAX Defense : " + str(max_defense)
    text += "<br>MAX Vitesse : " + str(max_vitesse)
    text += "<br>MAX Special Attaque : " + str(max_sattaque)
    text += "<br>MAX Special Defense : " + str(max_sdefense)

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

def list(request):
    result_pokemon = []
    pokemons_liste = Pokemon.objects.all()
    liste_pokemon = []
    for poke in pokemons_liste:
        type_liste = poke.types.all()
        type_couleur = couleur(type_liste)
        pokemon = {
            'nom' : poke.nom,
            'types' : type_liste,
            'image' : poke.front_image,
            'couleur' : type_couleur,
            'numero' : poke.numero
        }
        result_pokemon.append(pokemon)
    #print(result_pokemon)
    dict = {
        'pokemon' : result_pokemon,
    }
    return render(request, 'pokedexapp/liste.html',dict)

def home(request):
    return render(request, 'pokedexapp/home.html')

def detail(request, id):
    pokemon = Pokemon.objects.filter(numero=id)
    type_liste = pokemon[0].types.all()
    color = couleur(type_liste)
    dict = {
        'id' : id,
        'nom' : pokemon[0].nom,
        'taille' : pokemon[0].taille,
        'poids' : pokemon[0].poids,
        'pv' : pokemon[0].pv,
        'attaque' : pokemon[0].attaque,
        'defense' : pokemon[0].defense,
        'special_attaque' : pokemon[0].special_attaque,
        'special_defense' : pokemon[0].special_defense,
        'vitesse' : pokemon[0].vitesse,
        'image' : pokemon[0].front_image,
        'types' : type_liste,
        'couleur' : color,
    }
    return render(request, 'pokedexapp/detail.html', dict)

def couleur(type_liste):
    type_couleur = ""
    type_couleur2 = ""
    for x in type_liste:
        if(x.nom == 'fire'):
            type_couleur = 'fire'
        if(x.nom == 'grass'):
            type_couleur = 'grass'
        if(x.nom == 'water'):
            type_couleur = 'water'
        if(x.nom == 'electric'):
            type_couleur = 'electric'
        if(x.nom == 'bug'):
            type_couleur = 'grass'
        if(x.nom == 'normal'):
            type_couleur = 'normal'
        if(x.nom == 'poison'):
            type_couleur2 = 'poison'
        if(x.nom == 'ground'):
            type_couleur = 'ground'
        if(x.nom == 'fighting'):
            type_couleur2 = 'fire'
        if(x.nom == 'psychic'):
            type_couleur2 = 'psychic'
        if(x.nom == 'dragon'):
            type_couleur2 = 'fire'
        if(x.nom == 'rock'):
            type_couleur2 = 'ground'
        if(x.nom == 'flying'):
            type_couleur2 = 'water'
        if(x.nom == 'fairy'):
            type_couleur2 = 'psychic'
    if(type_couleur == ''):
        type_couleur = type_couleur2
    return type_couleur