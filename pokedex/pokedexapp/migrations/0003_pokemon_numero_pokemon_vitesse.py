# Generated by Django 4.1.2 on 2022-10-27 13:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pokedexapp', '0002_remove_pokemon_back_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='pokemon',
            name='numero',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='pokemon',
            name='vitesse',
            field=models.IntegerField(default=0),
        ),
    ]