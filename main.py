import discord
from discord.ext import commands
import requests
import os

intents = discord.Intents.default()
bot = commands.Bot(command_prefix='!', intents=intents)

@bot.command()
async def meteo(ctx, *, citta: str):
    # Usa la variabile d'ambiente per la chiave API o sostituiscila qui direttamente
    api_key =('39ffd633efd58a15bd966bd6f0d45403')
    # Definisci l'URL di base dell'API di OpenWeatherMap
    base_url = 'http://api.openweathermap.org/data/2.5/weather?'
    # Costruisci l'URL completo con la città specificata e la tua chiave API
    complete_url = f"{base_url}q={citta}&appid={api_key}&units=metric&lang=it"
    response = requests.get(complete_url)
    data = response.json()

    if data['cod'] == 200:
        temp = data['main']['temp']
        desc = data['weather'][0]['description']
        response_message = f"Tempo attuale a {citta}: {desc} con una temperatura di {temp}°C."
    else:
        response_message = "Città non trovata."
    
    await ctx.send(response_message)

@bot.event
async def on_ready():
    print(f'Bot pronto! Connesso come {bot.user.name}')

# Sostituisci 'il_tuo_token_di_bot_discord' con il token effettivo del tuo bot
token = 'MTE1NzYxOTY4NDkyMTg1MjAxNQ.GWdqCZ.SCwynt4cPPz6kkny9wFDCcT-Qm8ORsEa4ZjrZ0'
bot.run(token)