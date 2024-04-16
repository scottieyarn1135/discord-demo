#Imported packages
import os

#Discord packages
import discord

from discord.ext import commands

from discord.ui import Button, View

# Packages for API calls
import requests

import json

TOKEN = os.getenv('DISCORD_TOKEN')
NASA_KEY = os.getenv('NASA_KEY')

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

bot = commands.Bot(command_prefix='/', intents=intents)

@bot.command()
async def pokepicker(ctx,arg,arg2="Notshiny"):
    pokemon_api_url = "https://pokeapi.co/api/v2/pokemon/"

    pokemon_arg = arg

    pokemon_api_url_full = pokemon_api_url+pokemon_arg

    pokemon_response = requests.get(pokemon_api_url_full).json()

    pokemon_response_name = pokemon_response['name']

    view = View()

    pokedex_number = pokemon_response['id']

    non_shiny_pokemon_picture = pokemon_response['sprites']['other']['official-artwork']['front_default']

    shiny_pokemon_picture = pokemon_response['sprites']['other']['official-artwork']['front_shiny']

    template_embed = discord.Embed(
        colour=discord.Colour.dark_gold(),
        description=f'The pokedex number for {arg} is {pokedex_number} in the pokedex!',
        title=f'You have picked the pokemon {arg}!'
    )

    if arg2 == "shiny":
        template_embed.set_author(name=f'PokePicker')
        template_embed.set_image(url=f'{shiny_pokemon_picture}')
        await ctx.send(embed=template_embed, view=view)
    else:
        template_embed.set_author(name=f'PokePicker')
        template_embed.set_image(url=f'{non_shiny_pokemon_picture}')
        await ctx.send(embed=template_embed, view=view)


@bot.command()
async def quote_of_the_day(ctx):
    quote_of_the_day_url_request = requests.get('https://zenquotes.io/api/today').json()[0]
    quote_of_the_day_auther = quote_of_the_day_url_request['a']
    quote_of_the_day_quote = quote_of_the_day_url_request['q']
    quote_template = discord.Embed(
        colour = discord.Colour.dark_gold(),
        description = f'{quote_of_the_day_quote}',
        title = f'{quote_of_the_day_auther}'
    )
    await ctx.send(embed=quote_template)
@bot.command()
async def random_quote(ctx):
        random_quote_url_request = requests.get('https://zenquotes.io/api/random').json()[0]
        random_quote_auther = random_quote_url_request['a']
        random_quote = random_quote_url_request['q']
        random_quote_template = discord.Embed(
            colour = discord.Colour.dark_gold(),
            description = f'{random_quote}',
            title = f'{random_quote_auther}'
        )
        await ctx.send(embed=random_quote_template)
@bot.command()
async def space_picture_of_the_day(ctx):
        nasa_api_url = "https://api.nasa.gov/planetary/apod?api_key="
        nasa_api_url_full = f'{nasa_api_url}{NASA_KEY}'
        nasa_request = requests.get(nasa_api_url_full).json()
        nasa_media_url = nasa_request['url']
        nasa_title = nasa_request['title']
        nasa_description = nasa_request['explanation']
        nasa_template = discord.Embed(
            colour = discord.Colour.dark_gold(),
            description = f'{nasa_description} \n url for the media: {nasa_media_url}',
            title = f'{nasa_title}'
        )
        await ctx.send(embed=nasa_template)
bot.run(TOKEN)
