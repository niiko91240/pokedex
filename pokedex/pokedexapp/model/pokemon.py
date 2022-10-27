from django.db import models

class Type(models.Model):
    nom = models.CharField(max_length=40)

class Pokemon(models.Model):
    nom = models.CharField(max_length=40)
    type = models.CharField(max_length=20)
    taille = models.IntegerField(default=0)
    poids = models.IntegerField(default=0)
    pv = models.IntegerField(default=0)
    attaque = models.IntegerField(default=0)
    defense = models.IntegerField(default=0)
    special_attaque = models.IntegerField(default=0)
    special_defense = models.IntegerField(default=0)
    vitesse = models.IntegerField(default=0)
    front_image = models.URLField(default=None, blank=True)
    numero = models.IntegerField(default=0)
    types = models.ManyToManyField(Type)
