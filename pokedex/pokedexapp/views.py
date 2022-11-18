from urllib.request import Request
from django.shortcuts import get_object_or_404, render
from .model.pokemon import Pokemon, Type, Equipe
from django.http import HttpResponse
from django.template import loader
from asyncio.windows_events import NULL
import requests
import os
import random as rand   
from django.shortcuts import redirect
from django.db.models import Q


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

def list(request):
    request.session['lastpage'] = "list"
    result_pokemon = []
    if 'search2' not in request.POST:
        pokemons_liste = Pokemon.objects.all()
        param=''
    else:
        param = request.POST['search2']
        pokemons_liste = Pokemon.objects.filter(Q(types__nom__icontains=param) | Q(nom__icontains=param))
    pokemons_liste2 = []
    for i in pokemons_liste : 
        if i not in pokemons_liste2: 
            pokemons_liste2.append(i) 
    for poke in pokemons_liste2:
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
    dict = {
        'pokemon' : result_pokemon,
        'search' : param,
    }
    return render(request, 'pokedexapp/liste.html',dict)

def home(request):
    request.session['lastpage'] = "home"
    numero1=rand.randint(1,151)
    pokemonDiscover = [Pokemon.objects.get(numero=numero1)]
    numero2=rand.randint(1,151)
    if numero1 == numero2:
        while numero1==numero2: 
            numero2=rand.randint(1,151)
    pokemonDiscover.append(Pokemon.objects.get(numero=numero2))
    dict = {
        'pokemonDiscover' : pokemonDiscover,
    }
    return render(request, 'pokedexapp/home.html',dict)

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

def teams(request):
    request.session['lastpage'] = "teams"
    result_pokemon = []
    pokemons_liste = Pokemon.objects.all()
    for poke in pokemons_liste:
        type_liste = poke.types.all()
        type_couleur = couleur(type_liste)
        pokemon = {
            'nom' : poke.nom,
            'types' : type_liste,
            'image' : poke.front_image,
            'couleur' : type_couleur,
            'numero' : poke.numero,
            'front_image' : poke.front_image
        }
        result_pokemon.append(pokemon)
    
    
    result_teams = []
    teams_liste = Equipe.objects.all()
    for team in teams_liste:
        pokemon_team = team.pokemons.all()
        nb_pokemon_to_add = []
        for i in range(5-pokemon_team.count()):
            nb_pokemon_to_add.append(1)
        equipe = {
            'id' : team.pk,
            'nom' : team.nom,
            'pokemons' : pokemon_team,
            'nb_pokemons' : nb_pokemon_to_add
        }
        result_teams.append(equipe)


    dict = {
        'pokemon' : result_pokemon,
        'teams' : result_teams,
    }
    return render(request, 'pokedexapp/teams.html',dict)


def addTeam(request):
    request.session['lastpage'] = "teams"
    equipe = Equipe()
    equipe.nom = request.POST['teamName']
    equipe.save()
    return redirect('/pokedexapp/teams')
    

def deleteTeam(request):
    request.session['lastpage'] = "teams"
    equipe = Equipe.objects.get(id=request.POST['identifiant'])
    equipe.delete()
    return redirect('/pokedexapp/teams')

def addPokemon(request):
    request.session['lastpage'] = "teams"
    equipe = Equipe.objects.get(id=request.POST['idTeam'])
    pokemon = Pokemon.objects.get(numero=request.POST['idPokemon'])
    equipe.pokemons.add(pokemon)
    equipe.save()
    return redirect('/pokedexapp/teams')

def deletePokemon(request):
    request.session['lastpage'] = "teams"
    equipe = Equipe.objects.get(id=request.POST['idTeam'])
    pokemon = Pokemon.objects.get(numero=request.POST['idPokemon'])
    equipe.pokemons.remove(pokemon)
    equipe.save()
    return redirect('/pokedexapp/teams')