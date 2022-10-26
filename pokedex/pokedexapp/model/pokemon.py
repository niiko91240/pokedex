from django.db import models

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
    front_image = models.URLField()
    back_image = models.URLField()
